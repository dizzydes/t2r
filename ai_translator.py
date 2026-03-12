"""
AI Translator V2 - Uses OpenRouter LLM to translate Terraform to Railway
REBUILT FROM OFFICIAL RAILWAY LLM DOCS: https://docs.railway.com/api/llms-docs.md
"""

import json
import os
import requests


class AITranslator:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.max_retries = 3
        
    def translate(self, tf_data, cost_data=None):
        """
        Translate Terraform configuration to Railway using AI with retries
        Returns Railway configuration dictionary
        """
        if not self.api_key:
            print("   ❌ OPENROUTER_API_KEY not set in .env")
            return None
        
        # Build enhanced prompts with few-shot examples and chain-of-thought
        system_prompt = self._build_enhanced_system_prompt(tf_data)
        user_prompt = self._build_user_prompt(tf_data, cost_data)
        
        if self.verbose:
            print(f"   Sending request to OpenRouter...")
            print(f"   Terraform resources: {sum(len(v) for v in tf_data.get('resources', {}).values() if isinstance(v, list))}")
        
        # Retry logic with schema validation
        for attempt in range(self.max_retries):
            try:
                response = requests.post(
                    self.api_url,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                        "HTTP-Referer": "https://github.com/railway/terraform-migration-tool",
                        "X-Title": "Terraform to Railway Migration"
                    },
                    json={
                        "model": "anthropic/claude-3.5-sonnet",
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_prompt}
                        ],
                        "temperature": 0.3,
                        "max_tokens": 4000
                    }
                )
                
                if response.status_code != 200:
                    print(f"   ❌ OpenRouter API error: {response.status_code}")
                    if self.verbose:
                        print(f"   Response: {response.text}")
                    if attempt < self.max_retries - 1:
                        print(f"   ♻️  Retrying ({attempt + 2}/{self.max_retries})...")
                        continue
                    return None
                
                result = response.json()
                
                if "choices" not in result or len(result["choices"]) == 0:
                    print("   ❌ No response from AI")
                    if attempt < self.max_retries - 1:
                        print(f"   ♻️  Retrying ({attempt + 2}/{self.max_retries})...")
                        continue
                    return None
                
                content = result["choices"][0]["message"]["content"]
                
                if self.verbose:
                    print(f"   ✅ Received AI response ({len(content)} chars)")
                
                railway_config = self._parse_ai_response(content)
                
                # Validate schema
                if self._validate_schema(railway_config):
                    if self.verbose:
                        print(f"   ✅ Schema validation passed")
                    return railway_config
                else:
                    if attempt < self.max_retries - 1:
                        print(f"   ⚠️  Schema validation failed, retrying ({attempt + 2}/{self.max_retries})...")
                        continue
                    else:
                        print("   ⚠️  Schema validation failed on final attempt, returning anyway")
                        return railway_config
                
            except Exception as e:
                print(f"   ❌ Translation error: {e}")
                if self.verbose:
                    import traceback
                    traceback.print_exc()
                if attempt < self.max_retries - 1:
                    print(f"   ♻️  Retrying ({attempt + 2}/{self.max_retries})...")
                    continue
                return None
        
        return None
    
    def _build_enhanced_system_prompt(self, tf_data):
        """Build enhanced system prompt with context-aware additions"""
        base_prompt = self._build_system_prompt_v2()
        
        # Add few-shot examples for Lambda migrations
        if self._has_lambda(tf_data):
            base_prompt += self._get_lambda_examples()
        
        # Add chain-of-thought for complex migrations
        if self._is_complex(tf_data):
            base_prompt += self._get_chain_of_thought_instructions()
        
        return base_prompt
    
    def _build_system_prompt_v2(self):
        """Build system prompt FROM OFFICIAL Railway LLM docs"""
        return """You are an expert at migrating infrastructure to Railway platform.

SOURCE: Official Railway LLM Documentation (https://docs.railway.com/api/llms-docs.md)

=== RAILWAY ARCHITECTURE (OFFICIAL) ===

Railway organizes infrastructure:
- Workspace → billing/team scope
- Project → collection of services
- Environment → isolated config (production, staging)
- Service → deployable unit (app, database, or Function)
- Deployment → point-in-time release
- Volume → persistent storage (attached to services)
- Bucket → S3-compatible object storage

=== SERVICE TYPES (CRITICAL) ===

Railways has THREE types of Services:

1. **FUNCTION SERVICES** (Serverless - TRUE Lambda equivalent!)
   - Single-file TypeScript code (Bun runtime)
   - Max 96KB file size
   - Instant deploys (seconds)
   - Auto-install NPM packages on import
   - Perfect for: webhooks, simple APIs, cron jobs, event handlers
   - Can use Bun.serve() for HTTP endpoints
   - Can attach volumes
   - Supports cronSchedule for scheduled execution
   
2. **APP SERVICES** (Always-on containers)
   - Deployed from git repo, Docker image, or local code
   - Uses builders: RAILPACK (default) or DOCKERFILE
   - For complex apps, multi-file projects
   - Web (HTTP) or Worker (background) types
   
3. **DATABASE SERVICES** (Managed databases)
   - PostgreSQL, MySQL, MongoDB, Redis
   - Created via: railway add --database <type>
   - Auto-generate connection variables

=== LAMBDA MIGRATION DECISION TREE ===

For AWS Lambda → Railway:

```
Is Lambda code < 96KB and single-file logic?
  YES → Use Railway FUNCTION (recommended!)
       - Direct Lambda equivalent
       - Instant deploys
       - Lower cost for low-medium traffic
       - Example: webhook handlers, API endpoints, cron jobs
  
  NO → Use Railway SERVICE
      - For complex Lambda with many dependencies
      - Multi-file projects
      - Lambda Layers usage
      - >96KB code size
```

=== BUILDERS (OFFICIAL) ===

Only 2 builders exist:
- **RAILPACK**: Default, auto-detects language/framework
- **DOCKERFILE**: When Dockerfile exists in repo

⚠️ NIXPACKS is DEPRECATED - DO NOT USE!

Railway auto-uses Dockerfile if present, otherwise defaults to RAILPACK.

=== VOLUMES (OFFICIAL) ===

⚠️ CRITICAL: Railway has NO `railway volume` CLI commands!

Volumes configured ONLY via JSON config patches:
```bash
railway environment edit --json '{
  "services": {
    "<service-id>": {
      "volumeMounts": {
        "<volume-id>": {"mountPath": "/data"}
      }
    }
  }
}'
```

Users get IDs from: `railway status --json`

=== DATABASES (OFFICIAL) ===

CLI commands:
- `railway add --database postgres` ✅
- `railway add --database mysql` ✅
- `railway add --database redis` ✅  
- `railway add --database mongo` ✅ (NOT mongodb!)

Connection variables auto-created:
- Postgres: ${{Postgres.DATABASE_URL}}
- MySQL: ${{MySQL.MYSQL_URL}}
- Redis: ${{Redis.REDIS_URL}}
- MongoDB: ${{MongoDB.MONGO_URL}}

=== BUCKETS (OFFICIAL) ===

S3-compatible object storage.
Regions: sjc, iad, ams, sin

```bash
railway bucket create <name> --region sjc
railway bucket credentials --bucket <name> --json
```

=== CRON JOBS (OFFICIAL) ===

Supported in railway.json:
```json
{
  "deploy": {
    "cronSchedule": "0 */6 * * *",
    "startCommand": "node cron.js"
  }
}
```

Works for both Functions and Services!

=== PRICING (OFFICIAL as of 2026) ===

- RAM: $10/GB/month ($0.000231/GB/minute)
- CPU: $20/vCPU/month ($0.000463/vCPU/minute)
- Network Egress: $0.10/GB  
- Volume: $0.15/GB/month (250GB = $0.25/GB/month)
- Plans: Hobby $5 (includes $5 credit), Pro $20 (includes $20 credit)
- Pay per-minute for active resources

=== TRANSLATION RULES ===

**AWS Lambda → Railway Functions (FIRST CHOICE!)**
- Lambda HTTP API → Function with Bun.serve()
- Lambda webhook → Function  
- Lambda cron (<96KB) → Function with cronSchedule
- Lambda custom logic → Function (if <96KB single-file)

If Lambda has:
- Multiple files → Service
- Lambda Layers → Service  
- >96KB → Service
- Complex build → Service

**Other Compute → Services:**
- EC2/ECS/Fargate/Cloud Run → Service (type: web or worker)
- Use DOCKERFILE if Dockerfile exists, else RAILPACK

**Databases → Railway CLI:**
- RDS/Cloud SQL PostgreSQL → `railway add --database postgres`
- RDS/Cloud SQL MySQL →` railway add --database mysql`
- ElastiCache/Memorystore Redis → `railway add --database redis`
- DocumentDB/MongoDB → `railway add --database mongo`

**Storage:**
- EBS/EFS/Persistent Disk → Volume (JSON config patch only!)
- S3/GCS → Bucket

**Networking:**
- ALB/CloudFront/Load Balancer → Automatic (Railway built-in)
- VPC → Not needed (Railway private networking)
- API Gateway → Not needed (Functions/Services have HTTP)

**Services to KEEP on AWS/GCP:**
- MSK/Kafka (no managed Kafka on Railway)
- BigQuery (no data warehouse on Railway)
- Pub/Sub (no managed queue beyond Redis)
- Complex VPC networking

=== OUTPUT FORMAT ===

Return ONLY valid JSON (no explanatory text before/after):

```json
{
  "functions": [
    {
      "name": "handler-name",
      "description": "What it does",
      "code_template": "// TypeScript Bun code\nexport default {\n  async fetch(req: Request) {\n    return new Response('Hello');\n  }\n}",
      "cronSchedule": "0 * * * *",
      "environmentVariables": {"KEY": "value"},
      "estimatedSize_KB": 5,
      "notes": "Migration notes"
    }
  ],
  "services": [
    {
      "name": "service-name",
      "type": "web|worker",
      "source": ". or github-url",
      "builder": "RAILPACK|DOCKERFILE",
      "buildCommand": "npm install",
      "startCommand": "npm start",
      "cronSchedule": "0 */6 * * *",
      "environmentVariables": {"KEY": "value"},
      "volumes": [{"mountPath": "/data", "name": "data-vol", "size_gb": 10}],
      "healthcheckPath": "/health",
      "estimatedRAM_GB": 1.0,
      "estimatedCPU": 1.0
    }
  ],
  "databases": [
    {
      "type": "postgres|mysql|redis|mongo",
      "name": "db-name",
      "notes": "Usage notes"
    }
  ],
  "volumes": [
    {
      "name": "volume-name",
      "mount_path": "/data",
      "size_gb": 10
    }
  ],
  "buckets": [
    {
      "name": "bucket-name",
      "region": "sjc|iad|ams|sin",
      "notes": "Usage"
    }
  ],
  "migration_notes": {
    "easy_wins": ["Railway advantages"],
    "limitations": ["What Railway can't do"],
    "manual_steps": ["Required manual config"],
    "lambda_analysis": {
      "can_use_functions": true/false,
      "reason": "Why Functions vs Service choice was made",
      "code_size_estimate_kb": 10
    }
  }
}
```

=== CRITICAL REMINDERS ===

1. **Functions FIRST for Lambda** - They're the true equivalent!
2. **RAILPACK or DOCKERFILE only** - NO NIXPACKS!
3. **Volumes have NO CLI commands** - JSON patches only
4. **Mongo not mongodb** - Database naming matters
5. **Be honest about limitations** - BigQuery, MSK, Pub/Sub stay on cloud
6. **Use official Railway pricing** - Don't guess
7. **Return ONLY JSON** - No explanatory text before/after

Analyze carefully and provide practical, accurate Railway migrations."""

    def _build_user_prompt(self, tf_data, cost_data):
        """Build user prompt with Terraform data"""
        prompt = "# Terraform to Railway Migration Request\n\n"
        
        metadata = tf_data.get("metadata", {})
        if metadata:
            prompt += "## Project Information\n"
            prompt += f"- Cloud Provider: {metadata.get('cloud_provider', 'Unknown')}\n"
            prompt += f"- Application Type: {metadata.get('app_type', 'Unknown')}\n"
            
            resource_counts = metadata.get('resource_counts', {})
            if resource_counts:
                prompt += "\n### Resource Counts:\n"
                for category, count in resource_counts.items():
                    if count > 0:
                        prompt += f"- {category}: {count}\n"
        
        if cost_data:
            monthly_cost = cost_data.get('totalMonthlyCost', 0)
            prompt += f"\n## Current IaaS Cost\n"
            prompt += f"Monthly: ${monthly_cost}\n"
            
            if 'costByType' in cost_data:
                prompt += "\n### Cost Breakdown:\n"
                for res_type, cost in list(cost_data['costByType'].items())[:10]:
                    prompt += f"- {res_type}: ${cost:.2f}/month\n"
        
        resources = tf_data.get("resources", {})
        prompt += "\n## Terraform Resources to Migrate\n\n"
        
        for category, items in resources.items():
            if items and isinstance(items, list) and len(items) > 0:
                prompt += f"\n### {category.title()} ({len(items)} resources)\n"
                for item in items[:20]:
                    prompt += f"- {item.get('type', 'unknown')}: {item.get('name', 'unnamed')}\n"
        
        files = tf_data.get("files", [])
        if files:
            prompt += "\n## Sample Terraform Code\n\n"
            first_file = files[0]
            content = first_file.get("content", "")
            if len(content) > 2000:
                content = content[:2000] + "\n... (truncated)"
            prompt += f"### {first_file.get('name', 'main.tf')}\n```hcl\n{content}\n```\n"
        
        prompt += "\n\n---\n"
        prompt += "Analyze and provide Railway migration in JSON format."
        prompt += "\n**IMPORTANT: For Lambda functions, prefer Railway Functions over Services when possible!**"
        
        return prompt
    
    def _parse_ai_response(self, content):
        """Parse AI response - extract JSON with brace counting"""
        try:
            # Find JSON object
            first_brace = content.find("{")
            if first_brace == -1:
                raise ValueError("No JSON object found in response")
            
            # Count braces to find matching closing brace
            brace_count = 0
            last_brace = -1
            for i in range(first_brace, len(content)):
                if content[i] == '{':
                    brace_count += 1
                elif content[i] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        last_brace = i
                        break
            
            if last_brace == -1:
                raise ValueError("Unclosed JSON object")
            
            json_str = content[first_brace:last_brace+1].strip()
            
            if self.verbose:
                print(f"   Extracted JSON: {len(json_str)} chars")
            
            railway_config = json.loads(json_str)
            
            # Validate structure
            if not isinstance(railway_config, dict):
                raise ValueError("Response must be a dictionary")
            
            # Ensure required keys
            if "functions" not in railway_config:
                railway_config["functions"] = []
            if "services" not in railway_config:
                railway_config["services"] = []
            if "databases" not in railway_config:
                railway_config["databases"] = []
            if "cli_commands" not in railway_config:
                railway_config["cli_commands"] = []
            if "migration_notes" not in railway_config:
                railway_config["migration_notes"] = {}
            
            return railway_config
            
        except json.JSONDecodeError as e:
            print(f"   ❌ JSON parse error: {e}")
            if self.verbose:
                print(f"   Content: {content[:500]}")
            return None
        except Exception as e:
            print(f"   ❌ Parse error: {e}")
            return None
    
    def _validate_schema(self, railway_config):
        """Validate that railway_config has required structure"""
        if not railway_config or not isinstance(railway_config, dict):
            return False
        
        # Check required keys exist
        required_keys = ['functions', 'services', 'databases', 'migration_notes']
        for key in required_keys:
            if key not in railway_config:
                if self.verbose:
                    print(f"      Missing required key: {key}")
                return False
        
        # Validate each section has correct type
        if not isinstance(railway_config.get('functions'), list):
            return False
        if not isinstance(railway_config.get('services'), list):
            return False
        if not isinstance(railway_config.get('databases'), list):
            return False
        if not isinstance(railway_config.get('migration_notes'), dict):
            return False
        
        return True
    
    def _has_lambda(self, tf_data):
        """Check if Terraform contains Lambda resources"""
        resources = tf_data.get('resources', {})
        compute = resources.get('compute', [])
        
        for resource in compute:
            if 'lambda' in resource.get('type', '').lower():
                return True
        return False
    
    def _is_complex(self, tf_data):
        """Determine if migration is complex"""
        resources = tf_data.get('resources', {})
        total = sum(len(v) for v in resources.values() if isinstance(v, list))
        
        # Complex if >30 resources or contains MSK/BigQuery
        if total > 30:
            return True
        
        resources_str = str(resources).lower()
        if 'msk' in resources_str or 'bigquery' in resources_str or 'kafka' in resources_str:
            return True
        
        return False
    
    def _get_lambda_examples(self):
        """Add few-shot Lambda migration examples"""
        return """

=== FEW-SHOT EXAMPLES: Lambda → Railway Functions ===

Example 1: HTTP Lambda with API Gateway (VERIFIED 100% ACCURATE)
```
Terraform Input:
  - aws_lambda_function (handler: index.handler, runtime: nodejs18.x)
  - aws_apigatewayv2_api (HTTP API)

Correct Railway Output:
{
  "functions": [{
    "name": "api-handler",
    "description": "HTTP API handler (migrated from AWS Lambda)",
    "code_template": "export default {\\n  async fetch(req: Request) {\\n    return new Response('OK');\\n  }\\n}",
    "estimatedSize_KB": 10,
    "notes": "Railway Functions provide built-in HTTP - no API Gateway needed"
  }],
  "services": [],
  "lambda_analysis": {
    "can_use_functions": true,
    "reason": "HTTP-triggered Lambda behind API Gateway, estimated <96KB",
    "code_size_estimate_kb": 10
  }
}
```

Example 2: Cron Lambda (VERIFIED 100% ACCURATE)
```
Terraform Input:
  - aws_lambda_function (scheduled via CloudWatch Events)
  - aws_cloudwatch_event_rule (cron: 0 * * * *)

Correct Railway Output:
{
  "functions": [{
    "name": "cleanup-job",
    "cronSchedule": "0 * * * *",
    "code_template": "// Cleanup logic",
    "estimatedSize_KB": 5
  }],
  "lambda_analysis": {
    "can_use_functions": true,
    "reason": "Scheduled Lambda, simple logic, estimated <96KB"
  }
}
```

Example 3: Complex Lambda → Service (CORRECT PATTERN)
```
Terraform Input:
  - aws_lambda_function with Lambda Layers
  - Multiple Lambda functions sharing code

Correct Railway Output:
{
  "functions": [],
  "services": [{
    "name": "api-service",
    "type": "web",
    "notes": "Lambda has dependencies/layers, exceeds single-file limit"
  }],
  "lambda_analysis": {
    "can_use_functions": false,
    "reason": "Lambda uses Layers and multi-file architecture, requires Service"
  }
}
```
"""
    
    def _get_chain_of_thought_instructions(self):
        """Add chain-of-thought reasoning for complex migrations"""
        return """

=== CHAIN-OF-THOUGHT REASONING (for complex migrations) ===

For this complex infrastructure, follow this reasoning process:

STEP 1: Analyze what CAN migrate to Railway
- List compute resources (EC2, Lambda, ECS, Cloud Run, etc.)
- List databases (RDS, Cloud SQL, etc.)
- List storage (S3, GCS, etc.)

STEP 2: Identify what SHOULD STAY on cloud provider
- Check for: MSK, BigQuery, Pub/Sub, Kinesis, Redshift
- Check for: Complex VPC networking, ACM-PCA, IAP
- Document why these should stay

STEP 3: Map migrateable resources to Railway equivalents
- Lambda → Functions (if <96KB, single-file) OR Services
- EC2/ECS/Fargate/Cloud Run → Services
- RDS/Cloud SQL → Databases
- S3/GCS → Buckets

STEP 4: Generate configuration with detailed justification
- Include lambda_analysis for every Lambda
- Document easy_wins AND limitations honestly
- Provide manual steps for hybrid architecture if needed

Remember: Honesty about limitations builds trust!
"""
