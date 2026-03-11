# Railway Documentation

This file contains the complete Railway documentation structure and content for LLM consumption.

# Platform
Source: https://docs.railway.com/platform

# Philosophy
Source: https://docs.railway.com/platform/philosophy

Explore Railwayâs core philosophy and the principles that drive the Railway platform.

We design and develop Railway's product features to serve what we consider to be the three primary stages of software development:

- Development
- Deployment
- Diagnosis

Most developer-oriented products attempt to target one or more stages within the software development cycle. Railway provides solutions for developers for all of these stages, whereas some vendors focus on specific stages.

Railway is a company staffed with people who know developers would prefer to use tools they are familiar with. We believe software should be "take what you need, and leave what you don't." As a result, we are comfortable recommending additional vendors if they might acutely meet their needs. Railway's goal is for your unique need to be served so you can focus on delivering for your customers.

Companies should be as upfront as possible about their product and offerings to help you decide what is best for your team and users.

Let's talk about the number one use case: delivering apps to users in a Production environment. Railway, the company, is sustainable, building Railway's product, team, and company to last as long as your projects.

## Objective

The goal of this section is to describe the processes, internal and external that companies have requested in Railway's years of operation to help them build confidence to determine if Railway is a good fit for their company. Railway maintains a policy to be forthcoming and frank at all times. We would rather have a developer make the correct choice for their company than to adopt Railway and then come to regret that decision.

If you have any additional questions or if you require any additional disclosure you can contact us to set up a call at team@railway.com.

## Product philosophy

Railway is focused on building an amazing developer experience. Railway's goal is to enable developers to deploy their code and see their work in action, without thinking about CI/CD, deployments, networking, and so forth, until they need to.

### Take what you need

To achieve this goal, we've designed Railway to "just work", with all the necessary magic built in to achieve that. Railway at a high level reads your code repo, makes a best guess effort to build it into an OCI compliant image, and runs the image with a start command.

- Have a code repository but have yet to think about deployment? We got you. Connect your code repository and let Railway take care of the rest.
- Already built the perfect Dockerfile? Bring it. If you have a Dockerfile in your repo, we'll find it and use that to build your image.

If you've outgrown the "magic" built into deployment platforms, or are suspicious of things that are just too magical, we are happy to provide a high level overview of Railway's architecture.

### Leave what you don't

Streamlined deployment workflows and sane defaults are inherited by every project in Railway out of the box; but as a team of engineers, we at Railway are very aware that what works for one project does not always work for another. Or sometimes, you just need to be in control - maybe you already have a workflow you like, or maybe you need to layer Railway into existing infrastructure, and abstractions only get in your way.

That's why we've designed the platform for flexibility, wherever you need it.

On Railway, you can use the default pattern for deployment or opt to use vendor. In fact, we will even support you in your effort to integrate Railway in a unique way. Here are a couple of use cases we've helped customers take advantage of -

- Deploying to Railway from GitLab CI/CD
- Supporting the development of a Terraform provider
- Region based routing to workloads via Cloudflare

We love working with Railway's customers to solve interesting use cases. If you're not seeing a track for you, get in touch at team@railway.com and we'll find it!

## High-level architecture

As mentioned before, Railway at a high level takes your code, builds it, and throws it on running infrastructure on GCP. At a granular level Railway relies on a few systems to maintain workloads.

- Build Layer
  - Where archived folders of code or a Dockerfile (via GitHub or railway up) is sent to be built into an image
  - Railpack: Railway's build system that analyzes your code and generates optimized container images
  - Image Registry: either via Dockerhub/GitHub packages, or a previously built image from Railway's Build servers
- Deployment Layer
  - Where images are ran in containers, images are pulled from the Build Layer
  - Databases on Railway are images + volumes mounted on a machine
  - Cron services are containers ran on a defined schedule
- Routing Layer
  - This is the system that Railway maintains that routes requests into your running containers and provides private networks to suites of containers.
- Logging Layer
  - A suite of machines networked running Clickhouse that store container logs. This is accessed when you open the service logs pane.
- Dashboard Layer
  - Infrastructure and code that is used to manage the above layers.
  - This also includes any monitors that Railway uses to maintain the state of the Deployment Layer to maintain application state. (ex. Removing a deployment.)

Your code will either be in some, or all steps depending on the amount of Railway that you choose to adopt.

### Operational procedures

Railway uses a suite of alerting vendors, additional internal tools, and PagerDuty to ensure uptime of Railway's services described above. You can see Railway's uptime on the Instatus page. Operational incident management reports and RCAs are available by request for those on an Enterprise plan.

### Do I have to change how I write Code?

No, Railway is a deployment platform that works with your existing code. We don't require you to change how you write code or use any specific frameworks. We support all languages and frameworks that can be run in a Docker container or via Railpack.

### Is Railway serverless?

No, services on Railway are deployed in stateful Docker containers. The old deployments are removed on every new deploy.

We do have a feature, App Sleeping, that allows you to configure your service to "sleep" when it is inactive, and therefore will stop it from incurring usage cost while not in use.

## Book a demo

If you're looking to adopt Railway for your business, we'd love to chat and ensure your questions are answered. Click here to book some time with us.


# Use cases
Source: https://docs.railway.com/platform/use-cases

Explore real-world use cases for deploying and managing applications on Railway.

As mentioned in the philosophy document. Railway will make a best effort to provide all the information a developer needs to make the best choice for their workload.

## Is Railway production ready?

Many of Railway's customers use Railway to reliably deploy their applications to customers at scale. With that said, Production standards are going to be different depending on what your users expect. We have companies that use Railway in a variety of different verticals such as:

- Enterprise SaaS
- Consumer Social
- Education
- E-Commerce
- Crypto
- ML/AI
- Agencies

Companies on Railway range from hobby projects, to extremely fast growing startups, to publicly traded companies. Railway has been incrementally adopted from using the platform as a developer's scratchpad before writing Terraform to hand off to an Ops. team or being implemented end to end.

Railway's been in operation for now for more than three years and we have served billions of requests, with 100s of millions of deploys serving millions of end-users simultaneously.

## Railway scale

All of these verticals deploy workloads that may require high bandwidth operations or intensive compute.

However, service scale on the platform is not unbounded. As a foundational infrastructure company, we understand that customers may outpace Railway's pace of improvement for the platform. Even though 24 vCPU and 24 GB of memory sounds like a lot (with up to 42 replicas) on the Pro plan, when faced with hyper-growth: throwing more resources at the issue might be your best bet until long term optimizations can be made by your team.

Railway will gladly bump up your service limits within your tier of service to meet your needs. Even so, we will be frank and honest if you may need to seek elsewhere to augment your workloads with extra compute. If your compute needs outpace the Pro offering, consider the Enterprise plans where we offer even greater limits and capacity planning, email us to learn more, or click here to schedule some time to chat.

### Databases

We have customers using Railway's databases for their production environment with no issue. Railway's databases are optimized for a batteries included development experience. They are good for applications that are prioritizing velocity and iteration speed over scale.

Railway's databases are provided with no SLAs, are not highly available, and scale only to the limits of your plan. We don't think they are suitable for anything mission-critical, like if you wanted to start a bank.

We advise developers to:

- Configure backups
- Run-book and restore their backups
- Configure secondaries to connect to in-case of a disaster situation

As mentioned before: we don't believe in vendor lock-in here at Railway, if your needs outpace us, consider other vendors like PlanetScale (for MySQL) or Cockroach (for Postgres).

### Metrics

Railway provides up to 7 days worth of data on service information such as:

- CPU
- Memory
- Disk Usage
- Network

We also overlay commit and deployment behavior to correlate issues with application health to deployments. This is on top of the service logs that are continually delivered to users viewing a particular deployment of a service.

For service logs, we store logs for up to 90 days for Pro plan workspaces.

It is common for teams who wish to have additional observability to use an additional monitoring tool that maintains a longer time horizon of data such as New Relic, Sentry, or Datadog. Within projects, deploying a Datadog Agent is as easy as deploying the template and providing your Datadog API Keys.

### Networking

Railway doesn't have a hard bandwidth limit to the broader internet.

We may throttle your outbound bandwidth and reach out to you when it exceeds 100GB/month to ensure the legitimacy of your workloads. If you need to control where your traffic is allowed to come from such as setting up firewall rules, we recommend setting up Cloudflare or an external load balancer/L7 application firewall to handle it.

Private networking bandwidth is un-metered.

### Service level objectives

Railway does meet SLOs for companies who have greater need for incident, support, and business planning responsiveness. We provide this via Business Class, offered as an add-on to Pro plans and included in all Enterprise plans. More info.

### Will Railway exist in 10 years?

A common question we get in conversations with (rightly) skeptical developers is the above question. Most documentation pages don't address the meta question of a company's existence but how we run _our_ business affects yours.

The short and simple answer is: **Yes**.

Railway aims to exist for a very long time. Railway has presence on existing public clouds, while also building out presence on co-location providers. As a company, we have been structured sustainably with a first principles approach to every expense while growing sustainably.

### Unsupported use-cases

Unfortunately, the Railway platform isn't yet well-equipped to handle the following verticals that require extensive Gov't certification or GPU compute:

- Government
- Traditional Banking
- Machine Learning Compute

## General recommendations

A document like this can only go so far. We have a standing invitation for any team who needs an extended scale use-case to reach out to us directly by e-mailing team@railway.com, or via the Railway Discord server. You can also schedule some time with us directly by clicking here.

We would be happy to answer any additional questions you may have.


# Support
Source: https://docs.railway.com/platform/support

Learn about Railway's support channels.

subscription tiers. Support tier and prioritization is determined by 
your plan level.

## Support tiers

### Trial, free, hobby

Users on Trial, Free, and Hobby plans receive community support through 
Central Station or Discord. While Railway 
employees may participate in community discussions, responses are not 
guaranteed for these tiers.

### Pro 

Pro plan users get direct help from Railway via 
Central Station, usually within 72 hours. This excludes 
SLOs and application-level support.

### Enterprise & business class

For organizations requiring SLOs and enhanced support, please refer to 
Business Class support.

## How to ask for help

When you reach out for help, it's important that you help us help you. Please 
include as much information as you can, including but not limited to:

- Description of the issue you're facing
- IDs (Project ID, Service Name/ID, Deployment ID, etc.)
- Railway environment of your service/deployment
- Error messages and descriptions
- Logs (build and/or deploy)
- Link to GitHub repo/code or template you're using, if applicable

## Application-level support

Railway does not provide application-level support. We are unable to debug
your code or fix bugs in your application. We may provide these services on a 
case-by-case basis for Business Class or Enterprise 
customers.

For application-level support, connect with the Railway community on 
Central Station or 
Discord.

## Email support

Railway does not provide support via email. All support requests should be 
directed to Central Station or Discord. Email 
communication is reserved for the following specific purposes:

- Sales inquiries: team@railway.com
- Security reports: bugbounty@railway.com
- Abuse reports: abuse@railway.com
- Privacy inquiries: privacy@railway.com

Emails outside these categories may not receive a response.

## Central station

Railway conducts its support over the 
Central Station platform.

It hosts the Railway community of 1,800,000+ users and developers. It is where you can 
find answers to common questions, ask questions, and get in touch with the 
Railway team.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743120744/central-station_x3txbu.png"
alt="Screenshot of Railway Central Station"
layout="intrinsic"
width={1737} height={913} quality={100} />

Please ensure that you've searched for your issue before creating a new 
thread, follow the guidelines in 
How To Ask For Help, and abide by the 
Code of Conduct.

### Private threads

Pro users may create a **Private Thread** on 
Central Station. Private Threads are 
only visible to the creator and Railway employees.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1762527045/ask-railway-privately_lb3x33.png"
alt="Screenshot of Railway Central Station - Private Threads"
layout="intrinsic"
width={765} height={199} quality={100} />

Private Threads have a slower response time because only Railway employees can 
see them. 

Railway may make the thread public for community involvement if we determine 
that there is no sensitive information in your thread, or if you are asking
for application-level support.

## Discord

We have a vibrant Discord community of over 28,000+ users and developers. You 
can find the Railway Discord at https://discord.gg/railway.

Please ask your questions in the 
<a href="https://discord.com/channels/713503345364697088/1006629907067064482" target="_blank">â ï½ help</a> 
channel, and refrain from pinging anyone with the Team or Conductor roles.

## Slack

Railway offers Slack Connect channels to Enterprise plan customers with a 
minimum committed spend of $2,000/month. Customers can raise issues, coordinate 
their migration over to Railway, and provide feedback within a Slack Connect 
channel.

Additionally, the solutions team at Railway may provide a shared Slack Connect 
channel to facilitate better communication and support.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1733324712/docs/cs-2024-12-04-22.20_bms1sa.png"
alt="Screenshot of Slack"
layout="intrinsic"
width={571} height={743} quality={100} />

Enterprise teams with $2,000/month committed spend can create a Slack Connect 
channel within the Workspace settings page:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1733324438/docs/cs-2024-12-04-23.00_uvchnr.png"
alt="Screenshot of Slack Account Linking"
layout="intrinsic"
width={845} height={157} quality={100} />

Users in a Slack Connect channel can invite their team members using the Slack 
interface or by pressing the Join Slack button again to initiate new invites.

## Business class

For companies who need dedicated support, we offer Business Class.

Business Class is support and success designed for those who need the full 
attention of Railway. Business Class support is a dedicated support channel 
with SLOs for your company. Workspaces become eligible for Business Class 
support after $2,000/mo in spend.

Reach out to us at team@railway.com to enable your SLO.

### Business class SLOs

We prioritize Business Class customers over all other support requests.

| Severity                             | Acknowledgement Time |
| ------------------------------------ | -------------------- |
| P1 (Outages, Escalations)            | One hour - 24/7      |
| P2 (Bugs)                            | Same Business Day    |
| P3 (Integrations, General Questions) | Two Business Days    |

For Enterprise customers with $2,000/month committed spend who have a shared 
Slack Connect channel with us, you have access to "Critical" urgency level 
support requests:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1733325632/docs/cs-2024-12-04-23.20_smvweu.png"
alt="Screenshot of Critical urgency level in Slack"
layout="intrinsic"
width={392} height={255} quality={100} />

This feature is also available on Central Station for 
Business Class customers:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1762527110/emergency-help_ptt4wm.png"
alt="Screenshot of Emergency Help option in Central Station"
layout="intrinsic"
width={807} height={249} quality={100} />

Opening a Critical ticket allows you to page Railway's support on-call directly for 
an immediate response. Please only use this for production outages or critical 
platform issues preventing your team from using Railway.

### Definition of priorities

| Priority | Surface Areas                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | **Outages that impact production**. This covers the following components: incidents declared on <a href="https://status.railway.com/" target="_blank">status.railway.com</a> including and especially incidents with end-customer impact (e.g. inability to login to the Dashboard), customer workload-impacting issues due to high load requiring intervention from Railway (e.g. requiring additional resources beyond your current limits). |
| 2        | **Issues related to Railway features**. This covers features offered by Railway, including but not limited to the Dashboard, CLI, and platform-level features such as Deployments, Environments, Private Networking, Volumes.                                                                                                                                                                                                                  |
| 3        | **Integration work and general questions related to Railway**. This covers customer-related requests involving integrating Railway with other services (e.g. fronting your Railway workload with a DDoS protection service), leveraging tools to use Railway the way you like (e.g. IaC provisioning/Terraform), or questions about Railway features or its platform.                                                                          |

### Business class response hours

We offer support during business hours, and prioritize requests from Business 
Class customers:

- Business hours are Monday through Friday, 9am to 9pm Pacific Time
- Exceptions apply to Railway's business hours during P1 outages where the team will 
be on-call 24/7
- The team may reply outside of business hours, but we do not guarantee a 
response outside of business hours

### Business class resource limits

For Business Class customers, Railway increases resource limits beyond the 
standard limits on a need-based basis. Contact the team through your dedicated
communication channel to increase limits.

### Uptime calculation

As part of this offering, we agree to provide a monthly summary on the uptime 
of the components of Railway. Customers are provided an RCA to any outages on 
the Routing Layer.

### Compliance & audits

Security audits can be provided by request. For most customers, we can provide 
Railway's security and compliance documentation can be accessed via Railway's Trust 
Center at trust.railway.com. Please sign in with 
your Railway account's email address to access Trust Center.

## Enterprise

For enterprises, we offer everything in Business Class 
along with custom support tailored to your needs. Railway can enter into a 
contractual SLA under Railway's negotiated pricing offering. Reach out to us at 
team@railway.com for more information.


# Incident management
Source: https://docs.railway.com/platform/incident-management

Learn how Railway handles incident management.

Railway understands the importance of effective incident management procedures. We do what we can to minimize downtime, mitigate the impact of incidents, and ensure the smooth operation of Railway's systems. In the interest of transparency, we publish as much of Railway's procedure to keep Railway's customers in the know on how we handle and learn from incidents.

## Monitoring + reporting

Railway has a robust monitoring system in place to proactively detect and address any potential incidents. We continuously monitor Railway's infrastructure, including servers, networks, and applications, to ensure their smooth operation. By monitoring key metrics and performance indicators, we can identify any anomalies or potential issues before they escalate into full-blown incidents.

However, it's important to note that while we strive to stay ahead of incidents, there may be situations where unforeseen issues arise. In such cases, we rely on qualitative customer feedback to help us identify and address any issues promptly. We encourage Railway's customers to report any problems they encounter through the Railway Help Station, Slack, or Discord.

## Status page + uptime

Railway's uptime and incident retrospective can be accessed on the Railway Instatus page at https://railway.instatus.com/. On this page, you can view the historical uptime of Railway's systems and services. Additionally, you can find detailed information about past incidents, including retrospectives that provide insights into how incidents were handled and what measures were taken to prevent similar issues in the future.

For Enterprise customers, we offer SLOs and guarantees of service that may not be represented on the uptime dashboard.

## Incident severity

Railway catalogues incident's in the following buckets.

- **High**: the incident is potentially catastrophic to Railway Corporation and/or disrupts
  Railway Corporationâs day-to-day operations; violation of contractual requirements is likely. Ex. Any business level impact to 25 percent of Railway's customers for one hour or more. All incidents within this severity get public communications.
- **Medium**: the incident will cause harm to one or more business units within Railway
  Corporation and/or will cause delays to a customer business unitâs activities.
- **Low**: the incident is a clear failure of a component, but will not substantively impact the business. Railway still performs retrospectives within this severity.

### Responsible disclosure

Enterprise customers get Root Cause Analysis, and we attempt to publish event retrospectives on https://blog.railway.com/engineering


# Railway Metal
Source: https://docs.railway.com/platform/railway-metal

Railway Metal is Railwayâs own cloud infrastructure, built for high-performance, scalable, and cost-efficient app deployments. Learn how it works.

It is built on hardware that we own and operate in datacenters around the world.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1736893474/docs/m0_homdt8.png"
alt="Railway Metal Region"
layout="responsive"
width={1184} height={322} quality={80} />

Learn more about how we built it in the blog post So You Want to Build Your Own Data Center.

## Why?

We are making this move as part of Railway's commitment to providing best-in-class
infrastructure for Railway's users. This change enables us to improve the Railway platform's
performance, unlock additional features, increase reliability, and make
Railway more cost-effective for all users.

With Railway Metal, you can expect the following benefits:

- **Regions for Trial & Hobby plan users**: Railway Metal will be available to
  all users, including Trial & Hobby Plan users. Trial & Hobby plan users will
  be able to deploy services on all fRailway Metal regions in the US,
  Europe, and Southeast Asia.

- **Cheaper Pricing**: Running Railway's own hardware lets us reduce prices. Once
  Railway Metal is Generally Available, all users can expect to pay up to 50%
  less for Network Egress, and up to 40% less for Disk Usage.

- **Improved Performance**: Services on Railway will run faster. Railway's new CPUs
  are more powerful with higher core count and better performance per-core.
  Volume read/write performance will also be significantly faster as all
  of Railway's disks are NVMe SSDs, which are faster than the disks we could offer
  before.

- **Enhanced Reliability**: With Railway Metal, we are able to manage the
  hardware, software, and networking stack end-to-end. This allows us to move
  faster and fix problems more quickly. (For instance, before Railway Metal,
  incidents such as a single host failure would often take us ~60 minutes to bring the host back up. With Railway's own
  hardware, we can bring the host back up significantly faster.)

- **Improved Networking**: We connect directly to major internet providers and
  other cloud platforms worldwide, giving you faster connections in and out
  of Railway.

- **Higher Available Resources**: Railway Metal has greater capacity that we
  will be increasing over time, allowing us to offer you more computing
  resources on-demand.

- **Unlocks More Features**: With Railway's own hardware and networking stack, we
  can power more advanced features that were not possible before, such as
  Static Inbound IPs, Anycast Edge Network, High-Availability Volumes, etc.

## Metal edge network

Railway routes traffic through its own anycast Metal Edge network.

You can check if its enabled for your service in the Public Network section in the service settings tab.

<Image src="https://res.cloudinary.com/railway/image/upload/v1746495091/edge_enabled_pgferg.png"
alt="screenshot of a service with the metal edge network enabled"
layout="intrinsic"
width={910} height={254} quality={100} />

<span style={{'font-size': "0.9em"}}>Screenshot showing a domain with the Metal Edge Network enabled</span>

Benefits include better routing, less latency, and underlying infrastructure improvements.

## Regions & availability

Railway Metal is available to all users, including Trial & Hobby Plan users.

Each Railway Metal region is located in a datacenter that was chosen
strategically to provide the best possible performance and reliability.

We are in the process of expanding Railway Metal regions, and we expect to
have all regions available by the end of Q1'2025 (by 31 March 2025).

| Railway Metal Region       | Status    |
| -------------------------- | --------- |
| US West (California)       | ð¢ Active |
| US East (Virginia)         | ð¢ Active |
| Europe West (Amsterdam)    | ð¢ Active |
| Southeast Asia (Singapore) | ð¢ Active |

## Gradual upgrade

We will gradually move services without a volume
to Railway Metal as we increase the pool of Railway's hardware and its capabilities.

When this happens, you may see a new deploy initiated by Railway in your service:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1736969764/docs/m1_zw5m4f.png"
alt="Automatic upgrade banner"
layout="responsive"
width={1704} height={434} quality={80} />

Because this is a new deploy of your latest Active deployment, the behaviour
will be the same as if you've manually issued a new deploy. As such, you may
notice that:

- There may be a brief downtime during the upgrade. To prevent this, ensure
  you have Health Checks set up for your service

- All ephemeral storage (such as /tmp, etc.) will be wiped. To prevent this,
  use Volume to store data persistently. All storage is
  considered ephemeral unless they're on a Railway Volume

Note that the above generally applies to deploying a new version of
your service. The upgrade to Railway Metal is irrelevant to the behaviour
you may run into above - they are the same as if you were to manually deploy
a new version of your service.

For services in US West (Oregon), Railway will not move your service to
Railway Metal if your service references another service with a volume.
This is to prevent any cross-regional networking latency spikes for your
service. Refer to this FAQ for more information.

### Rollback

If you encounter any issues with your service after the upgrade, you can
rollback to the previous version by clicking Rollback button in the banner
above.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1736970652/docs/m4_rtxp2z.png"
alt="Automatic rollback"
layout="responsive"
width={1338} height={608} quality={80} />

### Manual rollback

To rollback manually, modify your service's Settings -> Deploy -> Regions
and select regions without the Metal (New) tag.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1736970930/docs/m3_kvwdgd.png"
alt="Manual rollback"
layout="responsive"
width={1140} height={560} quality={80} />

## Timeline

Railway's transition to Railway Metal will happen in phases. Here's what you can
expect:

| Date                         | What's Happening                                                                                                                                                          | Status |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Starting December 26th, 2024 | All new deploys on newly-created services without a volume by Trial & Hobby users will use Railway Metal by default.                                | ð¢     |
| Starting January 1st, 2025   | We will be gradually upgrading services _without a volume_ to Railway Metal. You can learn more about the gradual upgrade here. | ð¢     |
| Starting January 31st, 2025  | All new deploys on all services _without a volume_ by Trial & Hobby users will use Railway Metal by default.                                        | ð¢     |
| Starting February 14th, 2025 | All new deploys on all services _without a volume_ by Pro & Enterprise users will use Railway Metal by default.                                     | ð¢     |
| Starting March 14th, 2025    | All new deploys on services _with a volume_ by Trial & Hobby users will use Railway Metal by default.                                               | ð¢     |
| Starting March 21st, 2025    | We will begin migrating services to Railway metal for Hobby Users                                                                                                         | ð¢     |
| Starting March 28th, 2025    | All new deploys on services _with a volume_ by Pro & Enterprise users will use Railway Metal by default.                                            | ð¢     |
| Starting May 2nd, 2025       | We will begin migrating services to Railway metal for Pro Users                                                                                                           | ð¢     |
| Starting June 6th, 2025      | We will begin migrating services to Railway metal for Enterprise Users                                                                                                    | ð      |

The migration is aimed to be completed by the 4th of July, 2025.

## Pricing updates

If you migrate 80 percent of your workloads to Railway Metal, you'll benefit from significantly reduced costs:

- **Egress Fees**: Reduced by 50%, from $0.10/GB to $0.05/GB.
- **Disk Storage**: Reduced from $0.25/GB to $0.15/GB.

These pricing updates are automatically applied once 80 percent of your workloads are running on Railway Metal.

## FAQ

### Is this a free upgrade?

Yes.

### How do I receive the upgrade sooner?

Go to your service's Settings -> Deploy -> Regions, and select any region
with the Metal (New) tag.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1736970930/docs/m3_kvwdgd.png"
alt="Manual rollback"
layout="responsive"
width={1140} height={560} quality={80} />

Refer to Regions & Availability to see the regions
available for Railway Metal.

### How do I know if i'm on Railway metal?

To check if your service is running on Railway Metal, go to your service's
Settings -> Deploy -> Regions. If you are on Railway Metal, you will see a
Metal (New) tag next to the region.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1736970930/docs/m3_kvwdgd.png"
alt="Manual rollback"
layout="responsive"
width={1140} height={560} quality={80} />

### Is Railway metal stable?

Yes. We have been running a growing amount of deployments on it for the past
several months. As of the time of this writing, there are ~40,000 deployments
on Railway Metal, and we have not seen any significant issues.

### Is there downtime if I upgrade?

Upgrading to Railway Metal re-deploys your service. This may cause a brief
period of downtime as your new deploy is being set up. You can set up
Health Checks to prevent this.

### What is the difference between Railway metal and regions?

Railway Metal refers to Railway's own hardware and infrastructure. Regions refer to
the physical location of the datacenter where the hardware is located.

### I'm experiencing slow network performance after switching to us west (california) Railway metal region. What should I do?

You may experience increased latency if your application is communicating with
other services (such as databases) in US West (Oregon). This is caused by the
physical distance between Oregon (the current region) and California
(Railway Metal region).

We recommend switching back to the US West (Oregon) region if you are
experiencing increased latency after upgrading to US West (California).
See Manual rollback for instructions.

### Will Railway stay on gcp?

No. We are migrating completely onto Railway managed hardware. For customers who would like Railway to deploy into their public cloud, you can contact sales via the AWS Marketplace listing.

### Help! After migrating, why do I have increased latency?

It's likely that your database, or service with a volume, isn't migrated over to Metal. Stateful Metal is available starting March 2025. Users who migrate to a different region other than their stateful workload will see increased latency due to the additional physical distance from your service's region. Migrate when your desired region has stateful workloads available after March 2025.

### Why did my costs increase when moving to metal?

Although not intended, Railway Metal, has a different metrics sampler than the legacy hardware. This means that metrics will be quicker to come in, this also meant that legacy was undercounting the amount of resources on the previous hardware. As a result, some metrics like CPU will increase, others, like RAM will usually decrease.

### How do I opt-out?

There is no way to opt-out of Railway Metal. Please reach out to us
if you have any concerns.

## Getting help

Please reach out to us on the Railway Help Station if you run into any issues. You can also reach out to us over Slack if you are
a Pro or Business Class / Enterprise
customer.


# Priority boarding
Source: https://docs.railway.com/platform/priority-boarding

Priority Boarding is Railway's beta program for getting access early to new features. Learn how to be a part of it.

To read more about Priority Boarding, check out <a href="https://blog.railway.com/p/building-the-beta" target="_blank">Priority Boarding: The Journey to Get There</a>.

## Enable priority boarding

Visit the <a href="https://railway.com/account/feature-flags" target="_blank">Feature Flags page</a> in your account settings and flip the "Priority Boarding" switch to enable it.

Once enabled, any new features we release to Priority Boarding will automatically be enabled for your account.

<Banner variant="warning">
**Use Priority Boarding with caution if you have production workloads running**, as beta features may have unexpected behavior.
</Banner>

## Keep us posted

From this point forward, you'll have Priority Boarding features automatically enabled for your account. We'll notify you of any new features via the Changelog.

We kindly request that you report any issues you encounter on <a href="https://station.railway.com/" target="_blank">Central Station</a>.

That's all there is to it! Thanks for helping improve Railway, and we'll see you in Priority Boarding.


# Compare to Heroku
Source: https://docs.railway.com/platform/compare-to-heroku

Compare Railway and Heroku on infrastructure, pricing model and deployment experience.

- You can deploy your app from a Docker image or by importing your appâs source code from GitHub.
- Services are deployed to a long-running server.
- Connect your GitHub repository for automatic builds and deployments on code pushes.
- Create isolated preview environments for every pull request.
- Support for instant rollbacks.
- Integrated metrics and logs.
- Define Infrastructure-as-Code (IaC).
- Command-line-interface (CLI) to manage resources.
- Integrated build pipeline with the ability to define pre-deploy command.
- Custom domains with fully managed TLS, including wildcard domains.
- Run arbitrary commands against deployed services (SSH).

That said, there are some differences between the platforms that might make Railway a better fit for you.

## Scaling strategies

### Heroku

Heroku follows a traditional, instance-based model. Each instance has a set of allocated compute resources (memory and CPU).

In the scenario where your deployed service needs more resources, you can either scale:

- Vertically: you will need to manually upgrade to a large instance size to unlock more compute resources.
- Horizontally: your workload will be distributed across multiple running instances. You can either:
  - Manually specify the machine count.
  - Autoscale by defining a minimum and maximum instance count. The number of running instances will increase/decrease based on a target CPU and/or memory utilization you specify.

The main drawback of this setup is that it requires manual developer intervention. Either by:

- Manually changing instance sizes/running instance count.
- Manually adjusting thresholds because you can get into situations where your service scales up for spikes but doesnât scale down quickly enough, leaving you paying for unused resources.

Beyond scaling, there are other notable limitations. Heroku doesnât natively support multi-region deployments. To achieve that, you must create separate instances in different regions and set up an external load balancer to route traffic appropriately.

Furthermore, services deployed to the platform do not offer persistent data storage. Any data written to the local filesystem is ephemeral and will be lost upon redeployment, meaning you'll need to integrate with external storage solutions if your application requires data durability.

### Railway

Railway automatically manages compute resources for you. Your deployed services can scale up or down based on incoming workload without manual configuration of metrics/thresholds or picking instance sizes. Each plan includes defined CPU and memory limits that apply to your services.

You can scale horizontally by deploying multiple replicas of your service. Railway automatically distributes public traffic randomly across replicas within each region. Each replica runs with the full resource limits of your plan.

For example, if you're on the Pro plan, each replica gets 24 vCPU and 24 GB RAM. So, deploying 3 replicas gives your service a combined capacity of 72 vCPU and 72 GB RAM.

Replicas can be placed in different geographical locations for multi-region deployments. The platform automatically routes public traffic to the nearest region, then randomly distributes requests among the available replicas within that region. No need to define compute usage thresholds.

<video src="https://res.cloudinary.com/railway/video/upload/v1753470552/docs/comparison-docs/railway-replicas_nt6tz8.mp4" controls autoplay loop muted></video>

You can also set services to start on a schedule using a crontab expression. This lets you run scripts at specific times and only pay for the time theyâre running.

## Pricing

### Heroku

Heroku follows a traditional, instance-based pricing. You select the amount of compute resources you need from a list of instance sizes where each one has a fixed monthly price.

!Heroku instances

While this model gives you predictable pricing, the main drawback is you end up in one of two situations:

- Under-provisioning: your deployed service doesnât have enough compute resources which will lead to failed requests.
- Over-provisioning: your deployed service will have extra unused resources that youâre overpaying for every month.

Enabling horizontal autoscaling can help with optimizing costs, but the trade-off will be needing to figure out the right amount of thresholds instead.

Additionally, Heroku runs on AWS, so the unit economics of the business need to be high to offset the cost of the underlying infrastructure. Those extra costs are then passed down to you as the user, so you end up paying extra for:

- Unlocking additional features (e.g. private networking is a paid enterprise add-on).
- Pay extra for resources (e.g., bandwidth, memory, CPU and storage).

### Railway

Railway automatically scales your infrastructure up or down based on workload demands, adapting in real time without any manual intervention. This makes it possible to offer a usage-based pricing model that depends on active compute time and the amount of resources it consumes. You only pay for what your deployed services use.

You donât need to think about instance sizes or manually configure them. All deployed services scale automatically.

!Railway usage-based pricing

If you spin up multiple replicas for a given service, youâll only be charged for the active compute time for each replica.

Railway also has a serverless feature, which helps further reduce costs when enabled. When a service has no outbound requests for over 10 minutes, it is automatically put to sleep. While asleep, the service incurs no compute charges. It wakes up on the next incoming request, ensuring seamless reactivation without manual effort. This is ideal for workloads with sporadic or bursty traffic, so you only pay when your code is running.

Finally, Railwayâs infrastructure runs on hardware thatâs owned and operated in data centers across the globe. This means youâre not going to be overcharged for resources.

## Dashboard experience

### Heroku

Herokuâs unit of deployment is the app, and each app is deployed independently. If you have a different infrastructure components (e.g. API, frontend, background workers, etc.) they will be treated as independent entities. There is no topâlevel âprojectâ object that groups related apps.

Additionally, Heroku does not support shared environment variables across apps. Each deployed app has its own isolated set of variables, making it harder to manage secrets or config values shared across multiple services.

!Heroku dashboard

### Railway

Railwayâs dashboard offers a real-time collaborative canvas where you can view all of your running services and databases at a glance. You can group the different infrastructure components and visualize how theyâre related to one other.

You can also share environment variables between services, streamlining config management across complex projects with multiple components.

!Railway canvas

Additionally, Railway offers a template directory that makes it easy to self-host open-source projects with just a few clicks. If you publish a template and others deploy it in their projects, youâll earn a 25% kickback of their usage costs.

Check out all templates at railway.com/deploy

<video src="https://res.cloudinary.com/railway/video/upload/v1753470547/docs/comparison-docs/railway-templates-marketplace_v0svnv.mp4" controls autoplay loop muted></video>

## Summary

| **Category**                | **Heroku**                                                                                       | **Railway**                                                                                                      |
| --------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| **Scaling Model**           | Instance-based                                                                                   | Usage-based                                                                                                      |
| **Vertical Scaling**        | Manual upgrade to larger instance sizes                                                          | Auto-scales to the plan's limits without manual intervention                                                     |
| **Horizontal Scaling**      | Manual or threshold-based autoscaling; requires setting CPU/memory limits                        | Add replicas manually; traffic routed automatically across replicas and regions                                  |
| **Autoscaling Flexibility** | Threshold-based, needs manual tuning                                                             | Fully automated; scales based on workload                                                                        |
| **Multi-region Support**    | Not natively supported; must set up separate apps + external load balancer                       | Built-in; auto-routes traffic to nearest region and balances load across replicas                                |
| **Persistent Storage**      | Not supported; ephemeral file system only                                                        | Persistent volumes are supported                                                                                 |
| **Private Networking**      | Available with paid Enterprise add-on                                                            | Included at no extra cost                                                                                        |
| **Pricing Model**           | Fixed monthly pricing per instance size. Manual tuning required to avoid under/over-provisioning | Usage-based: Charged by active compute time Ã resource size (CPU & RAM). Inherently optimized by dynamic scaling |
| **Infrastructure Provider** | AWS-based; higher base costs                                                                     | Railway-owned global infrastructure; lower costs and no feature gating                                           |
| **Dashboard UX**            | Traditional app-based dashboard; each app is independent                                         | Visual, collaborative canvas view for full projects with interlinked services                                    |
| **Project Structure**       | No concept of grouped services/projects                                                          | Groups all infra components visually under a unified project view                                                |
| **Environment Variables**   | Isolated per app                                                                                 | Isolated per app but can be shared across services within a project                                              |
| **Wildcard Domains**        | Not supported; manual configuration needed per subdomain                                         | Fully supported; configure at the project level                                                                  |

## Migrate from Heroku to Railway

To get started, create an account on Railway. You can sign up for free and receive $5 in credits to try out the platform.

### Deploying your app

1. âChoose Deploy from GitHub repoâ, connect your GitHub account, and select the repo you would like to deploy.

!Railway onboarding new project

2. If your project is using any environment variables or secrets:
   1. Click on the deployed service.
   2. Navigate to the âVariablesâ tab.
   3. Add a new variable by clicking the âNew Variableâ button. Alternatively, you can import a .env file by clicking âRaw Editorâ and adding all variables at once.

!Railway environment variables

3. To make your project accessible over the internet, you will need to configure a domain:
   1. From the projectâs canvas, click on the service you would like to configure.
   2. Navigate to the âSettingsâ tab.
   3. Go to the âNetworkingâ section.
   4. You can either:
      1. Generate a Railway service domain: this will make your app available under a .up.railway.app domain.
      2. Add a custom domain: follow the DNS configuration steps.

## Need help or have questions?

If you need help along the way, the Railway Discord and Help Station are great resources to get support from the team and community.

Working with a larger workload or have specific requirements? Book a call with the Railway team to explore how we can best support your project.

## Code Examples

Total resources = number of replicas Ã maximum compute allocation per replica

Active compute time x compute size (memory and CPU)


# Compare to Render
Source: https://docs.railway.com/platform/compare-to-render

Compare Railway and Render on infrastructure, pricing model and dashboard experience.

- You can deploy your app from a Docker image or by importing your appâs source code from GitHub.
- Multi-service architecture where you can deploy different services under one project (e.g. a frontend, APIs, databases, etc.).
- Services are deployed to a long-running server.
- Services can have persistent storage via volumes.
- Public and private networking are included out-of-the-box.
- Healthchecks are available to guarantee zero-downtime deployments.
- Connect your GitHub repository for automatic builds and deployments on code pushes.
- Create isolated preview environments for every pull request.
- Support for instant rollbacks.
- Integrated metrics and logs.
- Define Infrastructure-as-Code (IaC).
- Command-line-interface (CLI) to manage resources.
- Integrated build pipeline with the ability to define pre-deploy command.
- Support for wildcard domains.
- Custom domains with fully managed TLS.
- Schedule tasks with cron jobs.
- Run arbitrary commands against deployed services (SSH).
- Shared environment variables across services.

That said, there are some differences between the platforms that might make Railway a better fit for you.

## Scaling strategies

### Render

Render follows a traditional, instance-based model. Each instance has a set of allocated compute resources (memory and CPU).

In the scenario where your deployed service needs more resources, you can either scale:

- Vertically: you will need to manually upgrade to a large instance size to unlock more compute resources.
- Horizontally: your workload will be distributed across multiple running instances. You can either:
  - Manually specify the machine count.
  - Autoscale by defining a minimum and maximum instance count. The number of running instances will increase/decrease based on a target CPU and/or memory utilization you specify.

The main drawback of this setup is that it requires manual developer intervention. Either by:

- Manually changing instance sizes/running instance count.
- Manually adjusting thresholds because you can get into situations where your service scales up for spikes but doesnât scale down quickly enough, leaving you paying for unused resources.

### Railway

Railway automatically manages compute resources for you. Your deployed services can scale up or down based on incoming workload without manual configuration of metrics/thresholds or picking instance sizes. Each plan includes defined CPU and memory limits that apply to your services.

You can scale horizontally by deploying multiple replicas of your service. Railway automatically distributes public traffic randomly across replicas within each region. Each replica runs with the full resource limits of your plan.

For example, if you're on the Pro plan, each replica gets 24 vCPU and 24 GB RAM. So, deploying 3 replicas gives your service a combined capacity of 72 vCPU and 72 GB RAM.

Replicas can be placed in different geographical locations for multi-region deployments. The platform automatically routes public traffic to the nearest region, then randomly distributes requests among the available replicas within that region. No need to define compute usage thresholds.

<video src="https://res.cloudinary.com/railway/video/upload/v1753470552/docs/comparison-docs/railway-replicas_nt6tz8.mp4" controls autoplay loop muted></video>

You can also set services to start on a schedule using a crontab expression. This lets you run scripts at specific times and only pay for the time theyâre running.

## Pricing

### Render

Render follows a traditional, instance-based pricing. You select the amount of compute resources you need from a list of instance sizes where each one has a fixed monthly price.

!Render instances

While this model gives you predictable pricing, the main drawback is you end up in one of two situations:

- Under-provisioning: your deployed service doesnât have enough compute resources which will lead to failed requests.
- Over-provisioning: your deployed service will have extra unused resources that youâre overpaying for every month.

Enabling horizontal autoscaling can help with optimizing costs, but the trade-off will be needing to figure out the right amount of thresholds instead.

Additionally, Render runs on AWS and GCP, so the unit economics of the business need to be high to offset the cost of the underlying infrastructure. Those extra costs are then passed down to you as the user, so you end up paying extra for:

- Unlocking additional features (e.g. horizontal autoscaling and environments are only available on paid plans).
- Pay extra for resources (e.g., bandwidth, memory, CPU and storage).
- Pay for seats where each team member you invite adds a fixed monthly fee regardless of your usage.

### Railway

Railway automatically scales your infrastructure up or down based on workload demands, adapting in real time without any manual intervention. This makes it possible to offer a usage-based pricing model that depends on active compute time and the amount of resources it consumes. You only pay for what your deployed services use.

You donât need to think about instance sizes or manually configure them. All deployed services scale automatically.

!Railway usage-based pricing

If you spin up multiple replicas for a given service, youâll only be charged for the active compute time for each replica.

Railway also has a serverless feature, which helps further reduce costs when enabled. When a service has no outbound requests for over 10 minutes, it is automatically put to sleep. While asleep, the service incurs no compute charges. It wakes up on the next incoming request, ensuring seamless reactivation without manual effort. This is ideal for workloads with sporadic or bursty traffic, so you only pay when your code is running.

Finally, Railwayâs infrastructure runs on hardware thatâs owned and operated in data centers across the globe. This means youâre not going to be overcharged for resources.

## Dashboard experience

### Render

Renderâs dashboard offers a traditional dashboard where you can view all of your projectâs resources.

!Render dashboard

### Railway

Railwayâs dashboard offers a real-time collaborative canvas where you can view all of your running services and databases at a glance. You can group the different infrastructure components and visualize how theyâre related to one another.

!Railway canvas

Additionally, Railway offers a template directory that makes it easy to self-host open-source projects with just a few clicks. If you publish a template and others deploy it in their projects, youâll earn a 25% kickback of their usage costs.

Check out all templates at railway.com/deploy

<video src="https://res.cloudinary.com/railway/video/upload/v1753470547/docs/comparison-docs/railway-templates-marketplace_v0svnv.mp4" controls autoplay loop muted></video>

## Summary

| **Category**             | **Render**                                                                                     | **Railway**                                                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Scaling Model**        | Instance-based                                                                                 | Usage-based                                                                                                                                |
| **Vertical Scaling**     | Manual upgrade to larger instance sizes.                                                       | Scales to plan limits automatically                                                                                                        |
| **Horizontal Scaling**   | Manually add/remove instances or autoscaling (based on CPU/memory thresholds); requires tuning | Manually add replicas, traffic is routed automatically across regions and replicas                                                         |
| **Multi-region Support** | Not supported                                                                                  | Built-in support; traffic routed to nearest region                                                                                         |
| **Pricing Model**        | Fixed monthly pricing per instance size. Seat-based pricing                                    | Usage-based: charged by active compute time Ã compute size. You don't pay for seats. You can invite your whole team for no additional cost |
| **Cost Optimization**    | Requires tuning to avoid over/under-provisioning                                               | Inherently optimized. Pay only for used compute                                                                                            |
| **Infrastructure**       | Runs on AWS and GCP; feature access and resources cost more                                    | Railway-owned global infrastructure, lower unit costs and features aren't gated                                                            |
| **Dashboard UX**         | Traditional dashboard to view project resources                                                | Real-time collaborative canvas with visual infra relationships. Template directory for 1-click deployments                                 |

## Migrate from Render to Railway

To get started, create an account on Railway. You can sign up for free and receive $5 in credits to try out the platform.

### Deploying your app

1. âChoose Deploy from GitHub repoâ, connect your GitHub account, and select the repo you would like to deploy.

!Railway onboarding new project

2. If your project is using any environment variables or secrets:
   1. Click on the deployed service.
   2. Navigate to the âVariablesâ tab.
   3. Add a new variable by clicking the âNew Variableâ button. Alternatively, you can import a .env file by clicking âRaw Editorâ and adding all variables at once.

!Railway environment variables

3. To make your project accessible over the internet, you will need to configure a domain:
   1. From the projectâs canvas, click on the service you would like to configure.
   2. Navigate to the âSettingsâ tab.
   3. Go to the âNetworkingâ section.
   4. You can either:
      1. Generate a Railway service domain: this will make your app available under a .up.railway.app domain.
      2. Add a custom domain: follow the DNS configuration steps.

## Need help or have questions?

If you need help along the way, the Railway Discord and Help Station are great resources to get support from the team and community.

Working with a larger workload or have specific requirements? Book a call with the Railway team to explore how we can best support your project.

## Code Examples

Total resources = number of replicas Ã maximum compute allocation per replica

Active compute time x compute size (memory and CPU)


# Compare to Fly
Source: https://docs.railway.com/platform/compare-to-fly

Compare Railway and Fly.io on deployment model, scaling, pricing and developer workflow.

- You can deploy your app from a Docker image or by importing your appâs source code from GitHub.
- Apps are deployed to a long-running server.
- Apps can have persistent storage through volumes.
- Public and private networking are included out-of-the-box.
- Multi-region deployments.
- Both platformsâ infrastructure runs on hardware thatâs owned and operated in data centers across the globe.
- Healthchecks to guarantee zero-downtime deployments.

That said, there are differences between both platforms when it comes to the overall developer experience that can make Railway a better fit for you.

## Deployment model & scaling

### Fly

When you deploy your app to Fly, your code runs on lightweight Virtual Machines (VMs) called Fly Machines. Each machine needs a defined amount of CPU and memory. You can either choose from preset sizes or configure them separately, depending on your appâs needs.

Machines come with two types of virtual CPUs: shared and performance.

Shared CPUs are the more affordable option. They guarantee a small slice of CPU time (around 6%) but can burst to full power when thereâs extra capacity. This makes them ideal for apps that are mostly idle but occasionally need to handle traffic, like APIs or web servers. Just keep in mind that heavy usage can lead to throttling.

Performance CPUs, by contrast, give you dedicated access to the CPU at all times. Thereâs no bursting or throttling, making them a better choice for workloads that require consistent, high performance.

**Scaling your app**

When scaling your app, you have one of two options:

- Scale a machineâs CPU and RAM: you will need to manually pick a larger instance. You can do this using the Fly CLI or API.
- Increase the number of running machines. There are two options:
  - You can manually increase the number of running machines using the Fly CLI or API.
  - Fly can automatically adjust the number of running or created Fly Machines dynamically. Two forms of autoscaling are supported.
    - Autostop/autostart Machines: You create a âpoolâ of Machines in one or more regions and Flyâs Proxy start/suspend Machines based on incoming requests. With this option, Machines are never created or deleted, you need to specify how many machines your app will need.
    - Metrics-based autoscaling: this is not supported out-of-the-box. However, you can deploy fly-autoscaler which polls metrics and automatically creates/deletes or starts/stops existing Machines based on the metrics you define.

!Scaling your app on Fly.io

### Railway

Railway automatically manages compute resources for you. Your deployed services can scale up or down based on incoming workload without manual configuration of metrics/thresholds or picking instance sizes. Each plan includes defined CPU and memory limits that apply to your services.

You can scale horizontally by deploying multiple replicas of your service. Railway automatically distributes public traffic randomly across replicas within each region. Each replica runs with the full resource limits of your plan.

For example, if you're on the Pro plan, each replica gets 24 vCPU and 24 GB RAM. So, deploying 3 replicas gives your service a combined capacity of 72 vCPU and 72 GB RAM.

Replicas can be placed in different geographical locations. The platform automatically routes public traffic to the nearest region, then randomly distributes requests among the available replicas within that region.

<video
src="https://res.cloudinary.com/railway/video/upload/v1753083716/docs/replicas_dmvuxp.mp4"
muted
autoplay
loop
controls>

Add replicas to your service

</video>

You can also set services to start on a schedule using a crontab expression. This lets you run scripts at specific times and only pay for the time theyâre running.

## Pricing

### Fly

Fly charges for compute based on two primary factors: machine state and CPU type (shared vs. performance).

Machine state determines the base charge structure. Started machines incur full compute charges, while stopped machines are only charged for root file system (rootfs) storage. The rootfs size depends on your OCI image plus containerd optimizations applied to the underlying file system.

Pricing for different preset sizes is available in Fly's documentation. You can get a discount by reserving compute time blocks. This requires paying the annual amount upfront, then receiving monthly credits equal to the "per month" rate. Credits expire at month-end and do not roll over to subsequent months. The trade-off is you might end up paying for unused resources.

!Fly compute presets pricing

One important consideration is that Fly Machines incur cost based _on running time_. Even with zero traffic or resource utilization, you pay for the entire duration a machine remains in a running state. While machines can be stopped to reduce costs, any time spent running generates full compute charges regardless of actual usage.

### Railway

Railway follows a usage-based pricing model that depends on how long your service runs and the amount of resources it consumes.

If you spin up multiple replicas for a given service, youâll only be charged for the active compute time for each replica.

!Railway autoscaling

Railway also has a serverless feature, which helps further reduce costs when enabled. When a service has no outbound requests for over 10 minutes, it is automatically put to sleep. While asleep, the service incurs no compute charges. It wakes up on the next incoming request, ensuring seamless reactivation without manual effort. This is ideal for workloads with sporadic or bursty traffic, so you only pay when your code is running.

## Developer workflow & CI/CD

### Fly

Fly provides a CLI-first experience through flyctl, allowing you to create and deploy apps, manage Machines and volumes, configure networking, and perform other infrastructure tasks directly from the command line.

However, Fly lacks built-in CI/CD capabilities. This means you can't:

- Create isolated preview environments for every pull request.
- Perform instant rollbacks.

To access these features, you'll need to integrate third-party CI/CD tools like GitHub Actions.

Similarly, Fly doesn't include native environment support for development, staging, and production workflows. To achieve proper environment isolation, you must create separate organizations for each environment and link them to a parent organization for centralized billing management.

For monitoring, Fly automatically collects metrics from every application using a fully-managed Prometheus service based on VictoriaMetrics. The system scrapes metrics from all application instances and provides data on HTTP responses, TCP connections, memory usage, CPU performance, disk I/O, network traffic, and filesystem utilization.

The Fly dashboard includes a basic Metrics tab displaying this automatically collected data. Beyond the basic dashboard, Fly offers a managed Grafana instance at fly-metrics.net with detailed dashboards and query capabilities using MetricsQL as the querying language. You can also connect external tools through the Prometheus API.

!fly-metrics.net

Advanced features like alerting and custom dashboards require working with multiple tools and query languages, creating a learning curve for teams wanting sophisticated monitoring capabilities.

Additionally, Fly doesn't support webhooks, making it more difficult to build integrations with external services.

### Railway

Railway follows a dashboard-first experience, while also providing a CLI. In Railway, you create a project for each app youâre building. A project is a collection of services and databases. This can include frontend, API, background workers, API, analytics database, queues and so much more. All in a unified deployment experience that supports real-time collaboration.

!Railway architecture

Additionally, Railway offers a template directory that makes it easy to self-host open-source projects with just a few clicks. If you publish a template and others deploy it in their projects, youâll earn a 25% kickback of their usage costs.

Check out all templates at railway.com/deploy

<video
src="https://res.cloudinary.com/railway/video/upload/v1753083712/docs/railway.com_templates_zcydjb.mp4"
muted
autoplay
loop
controls>

Railway templates

</video>

You also get:

- First-class support for environments so you can isolate production, staging, development, testing, etc.
- GitHub integration with support for provisioning isolated preview environments for every pull request.
- Ability to do instant rollbacks for your deployments.

Each Railway project includes a built-in observability dashboard that provides a customizable view into chosen metrics, logs, and data all in one place

!Screenshot of the Observability Dashboard

Finally, Railway supports creating webhooks which allow external services to listen to events from Railway

!Webhooks

## Summary

| Category                 | Railway                                                                            | Fly.io                                                                                                                                       |
| ------------------------ | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Scaling                  | Auto-scaling included (no manual config); supports horizontal scaling via replicas | Manual vertical/horizontal scaling or horizontal autoscaling (via fly-autoscaler); two autoscaling options (autostop/start, metrics-based) |
| Compute Pricing          | Usage-based where youâre only billed for active compute time                       | Based on machine uptime (started = full price); unused time still billed unless stopped                                                      |
| CI/CD Integration        | Built-in GitHub integration with preview environments and instant rollbacks        | No built-in CI/CD; requires third-party tools like GitHub Actions                                                                            |
| Environments Support     | First-class support for multiple environments (dev, staging, prod, etc.)           | Requires creating separate orgs per environment                                                                                              |
| Monitoring & Metrics     | Built-in observability dashboard (metrics, logs, data all in one place)            | Prometheus-based metrics + optional Grafana (fly-metrics.net) for deep dives                                                               |
| Webhooks & Extensibility | Webhook support for integrations                                                   | No support for outbound webhooks                                                                                                             |
| Developer Experience     | Dashboard-first, supports real-time team collaboration, CLI available              | CLI-first (flyctl) for all management tasks                                                                                                |

## Migrate from Fly.io to Railway

To get started, create an account on Railway. You can sign up for free and receive $5 in credits to try out the platform.

1. âChoose Deploy from GitHub repoâ, connect your GitHub account, and select the repo you would like to deploy.

   !Railway Deploy New Project

2. If your project is using any environment variables or secrets:
   1. Click on the deployed service.
   2. Navigate to the âVariablesâ tab.
   3. Add a new variable by clicking the âNew Variableâ button. Alternatively, you can import a .env file by clicking âRaw Editorâ and adding all variables at once.

!Railway Variables

3. To make your project accessible over the internet, you will need to configure a domain:
   1. From the projectâs canvas, click on the service you would like to configure.
   2. Navigate to the âSettingsâ tab.
   3. Go to the âNetworkingâ section.
   4. You can either:
      1. Generate a Railway service domain: this will make your app available under a .up.railway.app domain.
      2. Add a custom domain: follow the DNS configuration steps.

## Need help or have questions?

If you need help along the way, the Railway Discord and Help Station are great resources to get support from the team and community.

For larger workloads or specific requirements, you can book a call with the Railway team to explore how we can best support your project.

## Code Examples

Total resources = number of replicas Ã maximum compute allocation per replica

Active compute time x compute size (memory and CPU)


# Compare to Vercel
Source: https://docs.railway.com/platform/compare-to-vercel

Compare Railway and Vercel on infrastructure, pricing model and deployment experience.

- Git-based automated deployments with support for instant rollbacks.
- Automatic preview environments.
- Built-in observability.
- Autoscaling resources with usage-based pricing.

That said, there are fundamental differences between both platforms, and certain use cases where Railway is a better fit.

## Understanding the underlying infrastructure and ideal use cases

### Vercelâs infrastructure

Vercel has developed a proprietary deployment model where infrastructure components are derived from the application code (see Framework-defined infrastructure).

At build time, application code is parsed and translated into the necessary infrastructure components. Server-side code is then deployed as serverless functions, powered by AWS under the hood.

To handle scaling, Vercel creates a new function instance for each incoming request with support for concurrent execution within the same instance (see Fluid compute). Over time, functions scale down to zero to save on compute resources.

!https://vercel.com/blog/introducing-fluid-compute

This deployment model abstracts away infrastructure, but introduces limitations:

- Memory limits: the maximum amount of memory per function is 4GB.
- Execution time limit: the maximum amount of time a function can run is 800 seconds (~13.3 minutes).
- SizeÂ (after gzip compression): the maximum is 250 MB.
- Cold starts: when a function instance is created for the first time, thereâs an amount of added latency. Vercel includes several optimizations, which reduces cold start frequency but wonât completely eliminate them.

If you plan on running long-running workloads such as:

- Data Processing: ETL jobs, large file imports/exports, analytics aggregation.
- Media Processing: Video/audio transcoding, image resizing, thumbnail generation.
- Report Generation: Creating large PDFs, financial reports, user summaries.
- DevOps/Infrastructure: Backups, CI/CD tasks, server provisioning.
- Billing & Finance: Usage calculation, invoice generation, payment retries.
- User Operations: Account deletion, data merging, stat recalculations.

Or if you plan on running workloads that require a persistent connection such as:

- Chat messaging: Live chats, typing indicators.
- Live dashboards: Metrics, analytics, stock tickers.
- Collaboration: Document editing, presence.
- Live tracking: Delivery location updates.
- Push notifications: Instant alerts.
- Voice/video calls: Signaling, status updates.

Then deploying your backend services to Vercel functions will not be the right fit.

### Railwayâs infrastructure

Railway's underlying infrastructure runs on hardware thatâs owned and operated in data centers across the globe. By controlling the hardware, software, and networking stack end to end, the platform delivers best-in-class performance, reliability, and powerful features, all while keeping costs in check.

!Railway regions

Railway uses a custom builder that takes your source code or Dockerfile and automatically builds and deploys it, without needing configuration.

Your code runs on a long-running server, making it ideal for apps that need to stay running or maintain a persistent connection.

All deployments come with smart defaults out of the box, but you can tweak things as needed. This makes Railway flexible across different runtimes and programming languages.

Each service you deploy can automatically scale up vertically to handle incoming workload. You also get the option to horizontally scale a service by spinning up replicas. Replicas can be deployed in multiple regions simultaneously.

<video src="https://res.cloudinary.com/railway/video/upload/v1753470552/docs/comparison-docs/railway-replicas_nt6tz8.mp4" controls autoplay loop muted></video>

You can also set services to start on a schedule using a crontab expression. This lets you run scripts at specific times and only pay for the time theyâre running.

## Pricing model differences

Both platforms follow a usage-based pricing model, but are different due to the underlying infrastructure.

### Vercel

Vercel functions are billed based on:

- Active CPU: Time your code actively runs in milliseconds
- Provisioned memory: Memory held by the function instance, for the full lifetime of the instance
- Invocations: number of function requests, where youâre billed per request

Each pricing plan includes a certain allocation of these metrics.

This makes it possible for you to pay for what you use. However, since Vercel runs on AWS, the unit economics of the business need to be high to offset the cost of the underlying infrastructure. Those extra costs are then passed down to you as the user, so you end up paying extra for resources such as bandwidth, memory, CPU and storage.

### Railway

Railway follows a usage-based pricing model that depends on how long your service runs and the amount of resources it consumes.

!railway usage-based pricing

If you spin up multiple replicas for a given service, youâll only be charged for the active compute time for each replica.

Railway also has a serverless feature, which helps further reduce costs when enabled. When a service has no outbound requests for over 10 minutes, it is automatically put to sleep. While asleep, the service incurs no compute charges. It wakes up on the next incoming request, ensuring seamless reactivation without manual effort. This makes it ideal for sporadic or bursty workloads, giving you the flexibility of a full server with the cost efficiency of serverless, with the benefit of only paying when your code is running.

## Deployment experience

### Vercel

**Managing multiple services**

In Vercel, a project maps to a deployed application. If you would like to deploy multiple apps, youâll do it by creating multiple projects.

!Vercel dashboard

**Integrating your application with external services**

If you would like to integrate your app with other infrastructure primitives (e.g storage solutions for your applicationâs database, caching, analytical storage, etc.), you can do it through the Vercel marketplace.

!Vercel marketplace

This gives you an integrated billing experience, however managing services is still done by accessing the original service provider. Making it necessary to switch back and forth between different dashboards when youâre building your app.

### Railway

**Managing projects**

In Railway, a project is a collection of services and databases. This can include frontend, API, background workers, API, analytics database, queues and so much more. All in a unified deployment experience that supports real-time collaboration.

!Railway canvas

**Databases**

Additionally, Railway has first-class support for Databases. You can one-click deploy any open-source database:

- Relational: Postgres, MySQL
- Analytical: Clickhouse, Timescale
- Key-value: Redis, Dragonfly
- Vector: Chroma, Weviate
- Document: MongoDB

Check out all of the different storage solutions you can deploy.

Template directory

Finally, Railway offers a template directory that makes it easy to self-host open-source projects with just a few clicks. If you publish a template and others deploy it in their projects, youâll earn a 25% kickback of their usage costs.

Check out all templates at railway.com/deploy

<video src="https://res.cloudinary.com/railway/video/upload/v1753470547/docs/comparison-docs/railway-templates-marketplace_v0svnv.mp4" controls autoplay loop muted></video>

## Summary

| Feature                | Railway                                                             | Vercel                                                 |
| ---------------------- | ------------------------------------------------------------------- | ------------------------------------------------------ |
| Infrastructure Model   | Long-running servers on dedicated hardware                          | Serverless functions on AWS                            |
| Scaling                | Vertical + horizontal scaling with replicas                         | Scales via stateless function instances                |
| Persistent Connections | â Yes (sockets, live updates, real-time apps)                      | â Unsupported                                         |
| Cold Starts            | â No cold starts                                                   | â ï¸ Possible cold starts (with optimizations)           |
| Max Memory Limit       | Up to full machine capacity                                         | 4GB per function                                       |
| Execution Time Limit   | Unlimited (as long as the process runs)                             | 800 seconds (13.3 minutes)                             |
| Databases              | Built-in one-click deployments for major databases                  | Integrated via marketplace (external providers)        |
| Project Structure      | Unified project: multiple services + databases in one               | One service per project                                |
| Usage-Based Billing    | Based on compute time and size per replica                          | Based on CPU time, memory provisioned, and invocations |
| Ideal For              | Fullstack apps, real-time apps, backend servers, long-running tasks | Frontend-first apps, short-lived APIs                  |
| Support for Docker     | â Yes                                                              | â No (function-based only)                            |

## Migrate from Vercel to Railway

To get started, create an account on Railway. You can sign up for free and receive $5 in credits to try out the platform.

### Deploying your app

1. âChoose Deploy from GitHub repoâ, connect your GitHub account, and select the repo you would like to deploy.

!Railway onboarding new project

2. If your project is using any environment variables or secrets:
   1. Click on the deployed service.
   2. Navigate to the âVariablesâ tab.
   3. Add a new variable by clicking the âNew Variableâ button. Alternatively, you can import a .env file by clicking âRaw Editorâ and adding all variables at once.

!Railway environment variables

3. To make your project accessible over the internet, you will need to configure a domain:
   1. From the projectâs canvas, click on the service you would like to configure.
   2. Navigate to the âSettingsâ tab.
   3. Go to the âNetworkingâ section.
   4. You can either:
      1. Generate a Railway service domain: this will make your app available under a .up.railway.app domain.
      2. Add a custom domain: follow the DNS configuration steps.

## Need help or have questions?

If you need help along the way, the Railway Discord and Help Station are great resources to get support from the team and community.

Working with a larger workload or have specific requirements? Book a call with the Railway team to explore how we can best support your project.

## Code Examples

Active compute time x compute size (memory and CPU)


# Compare to DigitalOcean
Source: https://docs.railway.com/platform/compare-to-digitalocean

Compare Railway and DigitalOcean App Platform on infrastructure, pricing model and deployment experience.

- You can deploy your app from a Docker image or by importing your appâs source code from GitHub.
- Multi-service architecture where you can deploy different services under one project (e.g. a frontend, APIs, databases, etc.).
- Services are deployed to a long-running server.
- Public and private networking are included out-of-the-box.
- Healthchecks are available to guarantee zero-downtime deployments.
- Connect your GitHub repository for automatic builds and deployments on code pushes.
- Support for instant rollbacks.
- Integrated metrics and logs.
- Define Infrastructure-as-Code (IaC).
- Command-line-interface (CLI) to manage resources.
- Integrated build pipeline with the ability to define pre-deploy command.
- Support for wildcard domains.
- Custom domains with fully managed TLS.
- Run arbitrary commands against deployed services (SSH).
- Shared environment variables across services.
- Both platformsâ infrastructure runs on hardware thatâs owned and operated in data centers across the globe.

That said, there are some differences between the platforms that might make Railway a better fit for you.

## Scaling strategies

### DigitalOcean app platform

DigitalOcean App Platform follows a traditional, instance-based model. Each instance has a set of allocated compute resources (memory and CPU).

In the scenario where your deployed service needs more resources, you can either scale:

- Vertically: you will need to manually upgrade to a large instance size to unlock more compute resources.
- Horizontally: your workload will be distributed across multiple running instances. You can either:
  - Manually specify the machine count.
  - Autoscale by defining a minimum and maximum instance count. The number of running instances will increase/decrease based on a target CPU and/or memory utilization you specify.

The main drawback of this setup is that it requires manual developer intervention. Either by:

- Manually changing instance sizes/running instance count.
- Manually adjusting thresholds because you can get into situations where your service scales up for spikes but doesnât scale down quickly enough, leaving you paying for unused resources.

Beyond scaling, there are other notable limitations. DigitalOcean App Platform doesnât natively support multi-region deployments. To achieve that, you must create separate instances in different regions and set up an external load balancer to route traffic appropriately.

Furthermore, services deployed to the platform do not offer persistent data storage. Any data written to the local filesystem is ephemeral and will be lost upon redeployment, meaning you'll need to integrate with external storage solutions if your application requires data durability.

### Railway

Railway automatically manages compute resources for you. Your deployed services can scale up or down based on incoming workload without manual configuration of metrics/thresholds or picking instance sizes. Each plan includes defined CPU and memory limits that apply to your services.

You can scale horizontally by deploying multiple replicas of your service. Railway automatically distributes public traffic randomly across replicas within each region. Each replica runs with the full resource limits of your plan.

For example, if you're on the Pro plan, each replica gets 24 vCPU and 24 GB RAM. So, deploying 3 replicas gives your service a combined capacity of 72 vCPU and 72 GB RAM.

Replicas can be placed in different geographical locations for multi-region deployments. The platform automatically routes public traffic to the nearest region, then randomly distributes requests among the available replicas within that region. No need to define compute usage thresholds.

<video src="https://res.cloudinary.com/railway/video/upload/v1753470552/docs/comparison-docs/railway-replicas_nt6tz8.mp4" controls autoplay loop muted></video>

You can also set services to start on a schedule using a crontab expression. This lets you run scripts at specific times and only pay for the time theyâre running.

## Pricing

### DigitalOcean app platform

DigitalOcean App Platform follows a traditional, instance-based pricing. You select the amount of compute resources you need from a list of instance sizes where each one has a fixed monthly price.

!DigitalOcean App Platform instances

While this model gives you predictable pricing, the main drawback is you end up in one of two situations:

- Under-provisioning: your deployed service doesnât have enough compute resources which will lead to failed requests.
- Over-provisioning: your deployed service will have extra unused resources that youâre overpaying for every month.

Enabling horizontal autoscaling can help with optimizing costs, but the trade-off will be needing to figure out the right amount of thresholds instead.

### Railway

Railway automatically scales your infrastructure up or down based on workload demands, adapting in real time without any manual intervention. This makes it possible to offer a usage-based pricing model that depends on active compute time and the amount of resources it consumes. You only pay for what your deployed services use.

You donât need to think about instance sizes or manually configure them. All deployed services scale automatically.

!Railway usage-based pricing

If you spin up multiple replicas for a given service, youâll only be charged for the active compute time for each replica.

Railway also has a serverless feature, which helps further reduce costs when enabled. When a service has no outbound requests for over 10 minutes, it is automatically put to sleep. While asleep, the service incurs no compute charges. It wakes up on the next incoming request, ensuring seamless reactivation without manual effort. This is ideal for workloads with sporadic or bursty traffic, so you only pay when your code is running.

## Developer workflow & CI/CD

### DigitalOcean app platform

DigitalOcean App Platformâs dashboard offers a traditional dashboard where you can view all of your projectâs resources.

!DigitalOcean App Platform dashboard

However, DigitalOcean App Platform lacks built-in CI/CD capabilities around environments:

- No concept of âenvironmentsâ (e.g., development, staging, and production). To achieve proper environment isolation, you must create separate projects for each environment.
- No native support for automatically creating isolated preview environments for every pull request. To achieve this, you'll need to integrate third-party CI/CD tools like GitHub Actions.

Finally, DigitalOcean App Platform doesn't support webhooks, making it more difficult to build integrations with external services.

### Railway

Railwayâs dashboard offers a real-time collaborative canvas where you can view all of your running services and databases at a glance. You can group the different infrastructure components and visualize how theyâre related to one another.

!Railway canvas

Additionally, Railway offers a template directory that makes it easy to self-host open-source projects with just a few clicks. If you publish a template and others deploy it in their projects, youâll earn a 25% kickback of their usage costs.

Check out all templates at railway.com/deploy

<video src="https://res.cloudinary.com/railway/video/upload/v1753470547/docs/comparison-docs/railway-templates-marketplace_v0svnv.mp4" controls autoplay loop muted></video>

## Summary

| **Category**              | **DigitalOcean App Platform**                                                                                                         | **Railway**                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Scaling Model**         | Manual instance-based scaling                                                                                                         | Fully automated scaling                                                    |
| **Vertical Scaling**      | Manual upgrade to larger instance                                                                                                     | N/A â no instance sizes to manage                                          |
| **Horizontal Scaling**    | Manually add/remove instances or autoscaling (based on CPU/memory thresholds); requires tuning                                        | Deploy multiple replicas; traffic auto-distributed; no thresholds required |
| **Multi-region Support**  | Manual via separate instances and load balancers                                                                                      | Built-in support; traffic routed to nearest region                         |
| **Persistent volumes**    | Not supported                                                                                                                         | Supported                                                                  |
| **Pricing Model**         | Fixed monthly pricing per instance size                                                                                               | Usage-based: active compute time Ã memory/CPU used                         |
| **Cost Optimization**     | Requires tuning to avoid over/under-provisioning                                                                                      | Inherently optimized. Pay only for used compute                            |
| **Developer Dashboard**   | Traditional project dashboard                                                                                                         | Real-time collaborative canvas with visual service layout                  |
| **Environments & CI/CD**  | No native concept of environments, requires manual project setup. Automated preview deployments not supported. Webhooks not supported | Native support for preview environments, CI/CD integrations, and webhooks  |
| **Templates & Ecosystem** | Limited                                                                                                                               | Extensive template directory; creators can earn from deployed usage        |

## Migrate from DigitalOcean app platform to Railway

To get started, create an account on Railway. You can sign up for free and receive $5 in credits to try out the platform.

### Deploying your app

1. âChoose Deploy from GitHub repoâ, connect your GitHub account, and select the repo you would like to deploy.

!Railway onboarding new project

2. If your project is using any environment variables or secrets:
   1. Click on the deployed service.
   2. Navigate to the âVariablesâ tab.
   3. Add a new variable by clicking the âNew Variableâ button. Alternatively, you can import a .env file by clicking âRaw Editorâ and adding all variables at once.

!Railway environment variables

3. To make your project accessible over the internet, you will need to configure a domain:
   1. From the projectâs canvas, click on the service you would like to configure.
   2. Navigate to the âSettingsâ tab.
   3. Go to the âNetworkingâ section.
   4. You can either:
      1. Generate a Railway service domain: this will make your app available under a .up.railway.app domain.
      2. Add a custom domain: follow the DNS configuration steps.

## Need help or have questions?

If you need help along the way, the Railway Discord and Help Station are great resources to get support from the team and community.

Working with a larger workload or have specific requirements? Book a call with the Railway team to explore how we can best support your project.

## Code Examples

Total resources = number of replicas Ã maximum compute allocation per replica

Active compute time x compute size (memory and CPU)


# Compare to VPS
Source: https://docs.railway.com/platform/compare-to-vps

Compare Railway and VPS hosting on infrastructure management, security, monitoring, pricing, and operational overhead for modern applications.

VPS hosting providers like AWS EC2, DigitalOcean Droplets, Hetzner Cloud, Linode, or Vultr give you a virtual machine where you have full control over the operating system, software stack, and configuration. This offers maximum flexibility but requires significant DevOps expertise and ongoing maintenance.

Railway provides a fully managed platform that abstracts away infrastructure complexity while giving you the flexibility of a dedicated environment. You get VPS-level control without the operational burden.

## Quick comparison: VPS VS. Railway

| Dimension                  | VPS Hosting                                                                       | Railway                                                              |
| -------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Infrastructure**         | Full responsibility: OS setup, patches, SSL, firewalls, scaling                   | Zero-config deploy, managed OS/security, built-in scaling            |
| **Security & Compliance**  | Manual hardening, audits, SOC 2/ISO require major effort                          | SOC 2 Type II, GDPR, MFA, automatic patches, DDoS protection         |
| **Monitoring & Logging**   | Must integrate Prometheus/Grafana/ELK manually                                    | Built-in observability, logs, metrics, dashboards, alerting          |
| **Scaling & Distribution** | Manual vertical/horizontal scaling, DNS/load balancer setup, complex multi-region | Auto vertical/horizontal scaling, multi-region deploy with one click |
| **Pricing Model**          | Fixed monthly instance cost regardless of usage                                   | Usage-based, serverless sleeping, pay only for active compute        |
| **Workflow & Deployment**  | Manual CI/CD setup, manual rollbacks, secrets management                          | GitHub integration, preview envs, instant rollback, managed secrets  |

## Infrastructure & operational overhead

### VPS hosting

When you choose VPS hosting, you're essentially becoming your own infrastructure team. This means taking full responsibility for:

**Server Setup & Configuration**

* Installing and configuring the operating system (Ubuntu, CentOS, Debian, etc.)
* Applying security patches and system updates
* Configuring firewalls, SSH access, and user management
* Installing and configuring web servers (Nginx, Apache)
* Setting up reverse proxies and load balancers
* Managing SSL certificates and renewals

**Application Environment Management**

* Installing/managing programming runtimes (Node.js, Python, Go, etc.)
* Setting up process managers (PM2, systemd, supervisor)
* Configuring environment variables and secrets management
* Managing database installs/configs (MySQL, Postgres, MongoDB, etc.)
* Setting up caching layers (Redis, Memcached)

**System Administration**

* Monitoring disk space, memory usage, CPU performance
* Managing log rotation and aggregation
* Automated backups and disaster recovery planning
* Applying vulnerability patches
* DNS configuration and domain setup

Youâll need to continuously maintain and update this stack, troubleshoot outages, and scale resources as needed.

### Railway

Railway eliminates this operational burden:

**Zero-Configuration Deployment**

* Deploy directly from GitHub with automatic builds

!Railway deployment from GitHub

* Auto-detects dependencies and installs them
* Built-in support for major programming languages and frameworks
* Automatic SSL provisioning and renewal
* Health checks and automatic restarts

!Healthchecks

**Managed Infrastructure**

* Railway owns/operates underlying hardware
* Automatic OS/security patches
* Built-in load balancing and traffic distribution via service replicas
* Automatic scaling based on workload demand
* Managed networking with private service communication

## Security & compliance

### VPS hosting

Security is entirely your responsibility, including:

**Basic Security Hardening**

* Disable root login, enforce SSH key auth
* Configure firewalls (UFW/iptables)
* Install intrusion detection (fail2ban, IDS)
* Regular audits and patching

**Application Security**

* File permissions and ownership
* Secure headers (HSTS, CSP, X-Frame-Options)
* Rate limiting and DDoS protection
* Secure secret management
* Secure database connections

**Compliance Requirements**

Achieving certifications on VPS requires significant additional work:

* Access controls and audit logging
* Data classification/handling procedures
* Incident response/business continuity plans
* Security assessments & penetration testing
* Evidence collection and documentation
* Encryption/key management systems

This typically requires dedicated expertise and can be costly.

### Railway

Railway provides enterprise-grade security out of the box:

**Built-in Security Features**

* Encrypted secret/environment management

!Variables and secrets


* SSL/TLS encryption for all services
* Private networking within projects
* Automatic patches and updates
* DDoS protection

**Compliance & Certifications**

* SOC 2 Type II
* GDPR compliance
* HIPAA compliance
* Regular third-party audits

**Security Best Practices**

* Role-based access control

!Roles & permissions

* MFA and passkey support
* Regular assessments and penetration testing
* Incident response and continuity planning

## Monitoring & observability

### VPS hosting

Requires integrating multiple tools:

**System & Application Monitoring**

* Install agents (Prometheus, Grafana, commercial tools)
* Custom dashboards for CPU, memory, disk, network
* Configure alerting rules and notification channels
* Implement log aggregation/analysis (ELK, Loki)
* Uptime monitoring and health checks

### Railway

Monitoring is built-in:

**Observability Dashboard**

* CPU, memory, network metrics

!Observability dashboard

* Integrated log aggregation and search

!Logs

* Auto alerting and notifications
!Notifications

## Scalability & global distribution

### VPS hosting

Scaling requires manual setup:

**Vertical Scaling (Up)**

* Manually upgrade to larger instances
* Typically downtime during resizing
* Application restarts required
* Persistent storage resizing often requires downtime

**Horizontal Scaling (Out)**

* Provision additional VPS instances
* Configure load balancers (HAProxy, Nginx, cloud LB)
* Manage session persistence/sticky sessions
* Database connection pooling/discovery

**Multi-Region Deployment Challenges**

* Manual VPS setup in each region
* Complex DNS/georouting configs
* Data replication/sync complexity
* Cross-region latency
* Higher operational overhead and cost

### Railway

Scaling and distribution are automatic:

**Automatic Vertical Scaling**

* Scale up to plan limits automatically
* No downtime or manual intervention
* Live volume resizing without service interruption

**Effortless Horizontal Scaling**

* Deploy replicas with one click
!Horizontal scaling

* Automatic load balancing & health checks
* Automatic traffic routing to nearest region

**Multi-Region Deployment**

* Deploy globally with one command
!Multi-region deployment
* Auto traffic routing, failover, replication
* CDN integration for static assets
* Simplified data management
* Reduced latency for global users

## Pricing & cost optimization

### VPS hosting

* Fixed monthly pricing by instance size.
* Extra tools (monitoring, backups, scaling) often add hidden costs.

### Railway

Railway follows a usage-based pricing model that depends on how long your service runs and the amount of resources it consumes. You only pay for activce CPU and memory, not for idle time.

!railway usage-based pricing

Pricing plans start at $5/month. You can check out the pricing page for more details.

**Cost Optimization**

If you would like to further reduce costs, you can enable the serverless feature. When a service has no outbound requests for over 10 minutes, it is automatically put to sleep. While asleep, the service incurs no compute charges. It wakes up on the next incoming request, ensuring seamless reactivation without manual effort. This makes it ideal for sporadic or bursty workloads, giving you the flexibility of a full server with the cost efficiency of serverless, with the benefit of only paying when your code is running.

!serverless

## Developer workflow & deployment

### VPS hosting

Deploying requires building your own CI/CD:

**CI/CD**

* Configure GitHub Actions/Jenkins/etc.
* Write deployment scripts
* Separate staging/production setup
* Automated testing/quality gates
* Rollback procedures

**Environment Management**

* Manual env var config
* Separate servers for staging/prod
* Manual DB migrations/schema updates
* Complex secret management

### Railway

CI/CD and environments are built-in:

**Automatic CI/CD**

* GitHub repo integration
* Preview environments per pull request
* One-click rollbacks
* Automatic env var management

**Environment Management**

* Built-in support for dev/staging/prod

!Environment management

* Shared env vars across services
* Encrypted secret management
* Auto DB migrations/schema updates by customizing the pre-deploy command

## Railway as a VPS alternative: migrate from VPS to Railway

To get started, create an account on Railway. You can sign up for free and receive $5 in credits to try out the platform.

### Deploying your app

1. Choose "Deploy from GitHub repo", connect your GitHub account, and select the repo you would like to deploy.

!Railway onboarding new project

2. If your project is using any environment variables or secrets:
   1. Click on the deployed service.
   2. Navigate to the âVariablesâ tab.
   3. Add a new variable by clicking the âNew Variableâ button. Alternatively, you can import a .env file by clicking âRaw Editorâ and adding all variables at once.

!Railway environment variables

3. To make your project accessible over the internet, you will need to configure a domain:
   1. From the projectâs canvas, click on the service you would like to configure.
   2. Navigate to the âSettingsâ tab.
   3. Go to the âNetworkingâ section.
   4. You can either:
      1. Generate a Railway service domain: this will make your app available under a .up.railway.app domain.
      2. Add a custom domain: follow the DNS configuration steps.

## Need help or have questions?

If you need help along the way, the Railway Discord and Help Station are great resources to get support from the team and community.

Working with a larger workload or have specific requirements? Book a call with the Railway team to explore how we can best support your project.

## Code Examples

Active compute time x compute size (memory and CPU)



# Pricing
Source: https://docs.railway.com/pricing

# Plans
Source: https://docs.railway.com/pricing/plans

Learn about Railway's plans and pricing.



## Plans

Railway offers four plans in addition to a Trial:

|                |                                                                                                                                                    |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Free**       | For running small apps with $1 of free credit per month                                                                                             |
| **Hobby**      | For indie hackers and developers to build and deploy personal projects                                                                             |
| **Pro**        | For professional developers and their teams shipping to production                                                                                 |
| **Enterprise** | For teams building and deploying production applications with the need for enterprise features related to compliance, SLAs, and account management |

### Subscription pricing

Each Railway account needs an active subscription. The base subscription fee allows you to use the Railway platform and features included in the tier of your subscription. The subscription fee goes towards your usage-costs on the platform.

| Plan           | Price       |
| -------------- | ----------- |
| **Free**       | $0 / month  |
| **Hobby**      | $5 / month  |
| **Pro**        | $20 / month |
| **Enterprise** | Custom      |

Read more about Railway's plans at <a href="https://railway.com/pricing" target="_blank">railway.com/pricing</a>.

Curious about potential savings? Upload your current invoice and see how much you can save by running your workloads on Railway.

### Default plan resources

Depending on the plan you are on, you are allowed to use up these resources per service.

| Plan           | **Replicas** | **RAM**      | **CPU**        | **Ephemeral Storage** | **Volume Storage** | **Image Size** |
| -------------- | ------------ | ------------ | -------------- | --------------------- | ------------------ | -------------- |
| **Trial**      | **0**        | **1 GB**     | **2 vCPU**     | **1 GB**              | **0.5 GB**         | **4 GB**       |
| **Free**       | **0**        | **0.5 GB**   | **1 vCPU**     | **1 GB**              | **0.5 GB**         | **4 GB**       |
| **Hobby**      | **6**        | **48 GB**    | **48 vCPU**    | **100 GB**            | **5 GB**           | **100 GB**     |
| **Pro**        | **42**       | **1 TB**     | **1,000 vCPU** | **100 GB**            | **1 TB \***        | **Unlimited**  |
| **Enterprise** | **50**       | **2.4 TB**   | **2,400 vCPU** | **100 GB**            | **5 TB \***        | **Unlimited**  |

Note that these are maximum values and include replica multiplication.

\* For Volumes, Pro users and above can self-serve to increase their volume up to 250 GB. Check out this guide for information.

### Resource usage pricing

On top of the base subscription fee above, Railway charges for the resources that you consume.

You are only charged for the resources you actually use, which helps prevent runaway cloud costs and provides assurances that you're always getting the best deal possible on your cloud spend.

| Resource                                 | Resource Price                                        |
| ---------------------------------------- | ----------------------------------------------------- |
| **RAM**                                  | $10 / GB / month ($0.000231 / GB / minute)            |
| **CPU**                                  | $20 / vCPU / month ($0.000463 / vCPU / minute)        |
| **Network Egress**                       | $0.05 / GB ($0.000000047683716 / KB)                  |
| **Volume Storage** | $0.15 / GB / month ($0.000003472222222 / GB / minute) |

To learn more about controlling your resource usage costs, read the FAQ on How do I prevent spending more than I want to?

## Included usage

The Hobby plan includes $5 of resource usage per month.

If your total resource usage at the end of your billing period is $5 or less, you will not be charged for resource usage. If your total resource usage exceeds $5 in any given billing period, you will be charged the delta.

Included resource usage is reset at the end of every billing cycle and does not accumulate over time.

**Examples**:

- If your resource usage is $3, your total bill for the cycle will be $5. You are only charged the subscription fee because your resource usage is below $5 and therefore included in your subscription
- If your resource usage is $7, your total bill for the cycle will be $7 ($5 subscription fee + $2 of usage), because your resource usage exceeds the included resource usage

Similarly, the Pro plan includes $20 of resource usage per month and the same examples and billing logic apply. If your usage stays within $20, you'll only pay the subscription fee. If it exceeds $20, you'll be charged the difference on top of the subscription.

### Additional services

Railway offers Business Class Support as an add-on service to the Pro plan. Business Class Support is included with Enterprise. Contact us to get started.

## Image retention policy

Railway retains images for a period of time after a deployment is removed. This is to allow for rollback to a previous deployment.

| Plan             | **Policy**    |
| ---------------- | ------------- |
| **Free / Trial** | **24 hours**  |
| **Hobby**        | **72 hours**  |
| **Pro**          | **120 hours** |
| **Enterprise**   | **360 hours** |

When a deployment is removed, the image will be retained for the duration of the policy.

Rolling back a removed deployment within the retention policy will restore the previous image, settings, and all variables with a new deployment; no redeployment is required.

A removed deployment that is outside of the retention policy will not have the option to rollback; instead, you will need to use the redeploy feature. This will rebuild the image from the original source code with the deployment's original variables.

## One-time Grant of Credits on the Free Trial

Users who create a new Trial account receive a free one-time grant of $5. Railway will expend any free credit before consuming any purchased credits. Trial plan users are unable to purchase credits without upgrading to the Hobby plan.

Learn more about Railway's Free Trial here.

## Partial month charges

In some cases, your billing method may be charged for the partial amount of your bill earlier in the billing cycle.
This ensures that your account remains in good standing, and helps us mitigate risk and fraud.

## FAQs

### Which plan is right for me?

- **Hobby** is for indie hackers and developers to build and deploy personal projects
- **Pro** is for professional developers and their teams shipping to production
- **Enterprise** is for dev teams building and deploying production applications with the need for enterprise features related to compliance, SLAs, and account management

### Can I upgrade or downgrade at any time?

You can upgrade any time, and when you do, you will get to the features of your new plan, as well as access to more powerful resources, immediately. When you downgrade, the changes will take effect at the beginning of your next billing cycle.

### What is the difference between subscription and resource usage?

There are two main components to your bill:

| Component          | Description                                                             |
| ------------------ | ----------------------------------------------------------------------- |
| **Subscription**   | Cost of the plan you're on                                              |
| **Resource Usage** | Cost of the resources you've consumed: [cost per unit] x [used units] |

Subscription is a flat fee you pay monthly for the tier you're subscribed to, and Resource Usage varies according to your resource consumption for the month.

### Can I add collaborators to my project?

Railway's Pro and Enterprise plans are designed for collaboration. These plans allow you to add members to your workspace and manage their permissions.

Read more about adding members to your Pro or Enterprise workspace here.

### How long does Railway keep my volume data if I am no longer on a paid plan?

Railway will delete your data from the platform as per the timeline below after sufficient warning.

| Plan                   | Days                       |
| ---------------------- | -------------------------- |
| **Free or Trial plan** | 30 days after expiry       |
| **Hobby plan**         | 60 days after cancellation |
| **Pro plan**           | 90 days after cancellation |

### Is the hobby plan free?

No. The Hobby Plan is $5 a month, and it includes a resource usage credit of $5. Even if you do not use the $5 in usage (CPU, Memory, egress), you always pay the $5 subscription fee.

### Can I get the hobby plan subscription fee waived?

Railway waives the monthly Hobby plan subscription fee for a small set of active builders on the platform.

Eligibility is automatically assessed based on several factors, including your usage on the platform, your GitHub account, and more. If you qualify, you will be notified in the Dashboard or when you upgrade to the Hobby plan. If you do not qualify, you will not be eligible for the waiver.

This is a fully automated process, and Railway does not respond to requests for waiver.

### I prefer to prepay. Is that possible?

Not anymore as of March 30th, Railway requires the use of a post-paid card.

### What happens if I use credits as a payment method and my account runs out of credits?

If you are using credits as a payment method and your credit balance reaches zero, your subscription will be cancelled. You will no longer be able to deploy to Railway and we will stop all of your workloads. To resolve this, you will need to sign up for a new subscription after topping up sufficient credits.

### Why was I charged for a partial month of usage?

Railway has an automated system in place which can result in a partial amount of your bill being charged to your payment method, earlier in the billing cycle.

This is intended to ensure that your account remains in good standing, and helps us to mitigate risk and fraud.


# Free trial
Source: https://docs.railway.com/pricing/free-trial

Learn about Railway's free trial plan.

After 30 days passes or $5 is spent, the free trial reverts to the Free plan, which provides $1 of free credit per month. The credit does not roll over month to month.

## Full VS limited trial

Your trial experience depends on whether Railway can verify your account.

| Trial Type        | Deploy Code | Deploy Databases | Deploy Buckets | Network Access |
| ----------------- | ----------- | ---------------- | -------------- | -------------- |
| **Full Trial**    | â          | â               | â             | Full           |
| **Limited Trial** | â          | â               | â             | Restricted     |

When you sign up for a free Trial, you can connect your GitHub account to initiate verification. Your verification status depends on a number of factors, including the age and activity of your GitHub account.

If your account is not verified (either because you have not initiated the verification process or your account does not meet Railway's criteria for verification), your trial will have some network restrictions. Specifically, services on the Limited Trial have restricted outbound network access and only a limited set of ports are available.

Verification is a necessary measure to prevent abuse of the free Trial, limiting users from creating multiple accounts and reducing the risk of trial users deploying or hosting content that violates Railway's Terms of Service.

This is a fully automated process, and Railway does not respond to requests for verification. If your account is not verified, you can upgrade to the Hobby plan to unlock the full Railway experience.

## FAQs

### How do I get started with the free trial?

If you do not already have a Railway account, you can sign up for a free Trial by clicking "Login" at railway.com.

### How does the trial work?

When you sign up for the free Trial, you will receive a one-time grant of $5 in credits that you can use to try out Railway. The credits will be applied towards any usage on the platform and expire in 30 days.

If you upgrade to a plan while you still have a credit balance from the Trial, the remaining balance will carry over to your new plan. To prevent fraud and ensure your payment method is valid and in good standing, the carried-over Trial credits may not be applied to your first billing cycle, and will instead be applied as a discount to subsequent charges once a successful payment has been processed.

### What resources can I access during the trial?

During the trial, you can access the same features as on the Hobby plan, however you will be limited to 1 GB of RAM and shared (rather than dedicated) vCPU cores. Additionally, your projects will be limited to 5 services per project.

As a trial user, you can spin up databases and deploy code. However, if you are on the Limited Trial, your services will have some network restrictions.

### What's the difference between the limited trial and the full trial?

If you connect your GitHub account, and we are able to verify it against a set of parameters, you will be on the Full Trial with full network access.

If you do not connect a GitHub account, or we are not able to verify your account, you will be on the Limited Trial. You can still deploy code, databases, and buckets, but your services will have restricted outbound network access and only a limited set of ports will be available.

While you're on the Limited Trial, you can initiate verification at any time by visiting railway.com/verify in order to access the Full Trial experience.

### How far will the $5 one-time trial grant last?

The longevity of your one-time trial grant depends on how many resources you consume within the 30 day period you sign-up for the platform. The more resources you deploy, the greater the consumption.

### Data retention

Railway deletes stateful volumes created by Trial accounts 30 days after the expiration of your credits. To retain your data, upgrade your account after the Trial period.


# Understanding your bill
Source: https://docs.railway.com/pricing/understanding-your-bill

Learn how Railway billing works, why you're charged when idle, and how to read your invoice.



## How Railway billing works

Your subscription fee ($5 Hobby, $20 Pro) is a minimum usage commitment. It covers your first $5 or $20 of resource usage each month.

At the end of each billing cycle:
- **Usage â¤ plan amount**: You owe nothing extra, just your subscription for the next month
- **Usage > plan amount**: You pay the difference between your actual usage and what your plan already covered

Your invoice combines two periods:
- **Subscription** (billed in advance): Your minimum commitment for the upcoming month
- **Usage overage** (billed in arrears): Any resource usage from the previous month that exceeded your plan's included amount

**Example (Pro plan):** Your December 21 invoice includes:
- $20 Pro subscription for Dec 21 â Jan 21 (next month)
- $0 overage if Nov 21 â Dec 21 usage was under $20, OR the amount over $20 if you exceeded it

In some cases, Railway may charge a partial amount earlier in the billing cycle to ensure your account remains in good standing and to help mitigate fraud.

## Why you're charged when your app has no traffic

A common question: "Why am I being charged when my app has no traffic?"

The key concept is that **you pay for allocated resources, not traffic**. When your service is running, it consumes CPU and RAM regardless of whether it's actively handling requests.

Think of it like electricity: you pay for appliances that are plugged in and running, not just when you're actively using them. A server running idle still uses memory to stay loaded and CPU cycles to stay responsive.

### Solutions to reduce idle costs

| Solution                                            | Description                                              |
| --------------------------------------------------- | -------------------------------------------------------- |
| Serverless               | Automatically stops services when inactive               |
| Usage Limits             | Set spending caps to prevent unexpected charges          |
| Delete unused services                              | Remove services you no longer need                       |
| Private Networking    | Reduce egress costs by keeping traffic internal          |

## Understanding included usage

Both paid plans include a usage credit that offsets your resource consumption:

| Plan       | Subscription | Included Usage |
| ---------- | ------------ | -------------- |
| **Hobby**  | $5/month     | $5             |
| **Pro**    | $20/month    | $20            |

**How it works:**

1. Your subscription fee goes toward your resource usage
2. If usage stays within the included amount, you only pay the subscription fee
3. If usage exceeds the included amount, you pay the difference

**Examples (Hobby plan):**

| Resource Usage | Subscription | Included Usage Applied | Total Bill |
| -------------- | ------------ | ---------------------- | ---------- |
| $3             | $5           | $3                     | $5         |
| $5             | $5           | $5                     | $5         |
| $8             | $5           | $5                     | $8         |
| $15            | $5           | $5                     | $15        |

**Important:** Included usage credits reset each billing cycle. They do not accumulate or roll over to the next month. If you use $2 this month, you don't get $8 next month.

## Reading your invoice

Your Railway invoice contains several line items. Here's what each means:

<Image src="https://res.cloudinary.com/railway/image/upload/v1769474205/docs/bill_screenshot_elzqtf.png" alt="Example Railway invoice showing resource usage, subscription, included usage discount, and applied balance" width={1666} height={1546} quality={100} />

### Subscription charges

The flat fee for your plan appears as a line item:
- "Hobby plan" - $5.00
- "Pro plan" - $20.00

Pro and Enterprise workspaces also show a per-seat line item:
- "Pro (per seat)" - $0.00 (seats are free, this line just shows the member count)

### Resource usage charges

Resources are listed by type with the unit and billing period:

| Line Item                             | Meaning                                      |
| ------------------------------------- | -------------------------------------------- |
| "Disk (per GB / min)"                 | Volume storage charges                       |
| "Network (per MB)"                    | Outbound data transfer (egress) charges      |
| "vCPU (per vCPU / min)"               | CPU usage charges                            |
| "Memory (per MB / min)"               | RAM usage charges                            |

Each line item shows the quantity used, unit price, and total amount for the billing period.

### Included usage

Your plan's included usage appears as a discount in the invoice summary:
- "Hobby plan included usage ($5.00 off)"
- "Pro plan included usage ($20.00 off)"

The amount in parentheses shows the maximum credit available. The actual discount applied equals your resource usage up to that maximum. For example, if your resource usage is $15.39 on the Pro plan, you'll see "-$15.39" applied even though the max is $20.00.

### Applied balance

"Applied balance" appears in the invoice summary when you have account credits or small amounts carried forward:

- **Credit applied**: If you have credits on your account (from refunds, promotions, or previous overpayments), they appear as a negative "Applied balance" reducing your amount due
- **Small amounts deferred**: If your total invoice is less than $0.50, Railway marks it as paid and carries the amount forward to your next invoice

### Tax and VAT

If applicable based on your billing location, you may see:
- "Sales Tax" or "VAT" as a separate line item

Ensure your billing information is accurate to receive correct tax assessment.

## Common causes of unexpected charges

### High network egress

Network egress (outbound data transfer) is charged at $0.05/GB. Common causes of high egress:

- **Not using private networking for databases**: If your app connects to your Railway database using the public URL instead of the private URL, all that traffic counts as egress. Use DATABASE_URL (private) instead of DATABASE_PUBLIC_URL.
- **Large file transfers**: Serving large files, images, or videos directly from your service.
- **API responses**: High-traffic APIs returning large payloads.

**Solution:** Use private networking for all service-to-service communication within Railway.

### PR deploys / ephemeral environments

When you have PR deploys enabled, Railway creates a copy of your environment for each pull request. These environments run real services that consume real resources.

If you have 5 open PRs, you may be running 5x your normal workload.

**Solution:** Close PRs promptly or disable PR deploys if you don't need them.

### Idle services still running

Services consume resources even when not handling traffic. If you have development, staging, or test environments running continuously, they add up.

**Solution:** Enable Serverless on services that don't need to be always-on, or delete unused services.

### Memory leaks

If your application has a memory leak, it will gradually consume more RAM over time until it hits limits or gets restarted. This inflates your memory costs.

**Solution:** Monitor your service metrics for growing memory usage and fix leaks in your application code.

## Related resources

- Plans and Pricing - Detailed pricing information
- Pricing FAQs - Common pricing questions
- Optimize Usage - Guide to reducing costs
- Usage Limits - Set spending caps
- Serverless - Auto-stop inactive services
- Private Networking - Reduce egress costs


# FAQs
Source: https://docs.railway.com/pricing/faqs

General common Questions & Answers related to Railway's pricing.

### Can I try Railway without a credit-card?

Yes. As a new Railway user, you can sign up for a Free Trial. You will receive a one-time grant of $5 to use on resources.

### What payment methods are accepted?

Railway only accepts credit cards for plan subscriptions. We also support custom invoicing for customers on the Enterprise plan.

### What will it cost to run my app?

With Railway, you are billed for the subscription fee of the plan you're subscribed to, and the resource usage of your workloads.

To understand how much your app will cost to run on Railway, we recommend that you:

1. Deploy your project with the Trial or Hobby plan
2. Allow it to run for one week
3. Check your Estimated Usage in the Usage Section of your Workspace settings

Keeping it running for one week allows us to rack up sufficient metrics to provide you with an estimate of your usage for the current billing cycle. You can then use this information to extrapolate the cost you should expect.

We are unable to give exact quotes or estimates for how much it will cost to run your app because it is highly dependent on what you're deploying.


If you are supporting a commercial application, we highly recommend you to upgrade to the Pro plan for higher resource limits and access to priority support.

### How do I prevent spending more than I want to?

Check out the guide on cost control.

### Why is my resource usage higher than expected?

You can check your resource usage in the Usage Section of your Workspace settings. This includes a breakdown of your resource usage by project, along with the resource it's consuming (CPU, Memory, Network, etc.)

Common reasons for high resource usage include:

- Memory leaks in your application, causing it to consume more memory than necessary
- Higher traffic than usual, causing your app to consume more CPU and/or Network
- Certain templates or apps may be inherently more resource-intensive than others
- If you notice high egress cost in your bill, ensure that you are connecting to your Railway databases over Private Networking
- If you have PR deploys enabled in your project, Railway will deploy a mirror copy of your workload(s) based on the environment it forks from (productionÂ by default). You are billed for those workload(s) running in the ephemeral environment

Unfortunately, we are unable to assist with figuring out why your bill is higher than normal, as it is entirely dependent on what you have deployed. Resource usage is billed in a manner akin to how a utility company operates: they can tell you the amount of electricity you've consumed, but they can't explain the reasons for your high usage. Similarly, we can only provide information on the quantity of resources you consume, not the reasons behind it.

### Why am I charged for more than $5 on the hobby plan?

Railway's pricing has two components: a monthly subscription fee, and resource usage costs. While the Hobby plan includes $5 of resource usage per month, you are charged for any usage that exceeds this amount.

Learn more here.

### Why is there an "applied balance" on my invoice?

When the amount due on your invoice is less than $0.50, and you do not have a credit balance, Railway marks the invoice as paid and registers the amount to your credit balance as a debit to be charged on a future invoice.

### How do I view or upgrade my current plan?

Your current plan is listed in the Account Selector in the top left corner of your Dashboard. You can also view your active plan and upgrade options from the Plans page. 

### How do I cancel my subscription?

To cancel your active subscription, go to the "Active Plan" section of your Billing page and click Cancel Plan. 

When you cancel your subscription, Railway will stop all deployments in your workspace to prevent further charges. Your plan will remain active until the end of your billing cycle. 

### How do I add or update billing information?

To add or update your Billing information, go to the Billing page. In the "Billing Info" section, you can add or update the following information: 
- Payment Method
- Billing Email
- Billing Address
- Tax ID / VAT number

When Billing Information is added or updated, it will be reflected on all future invoices from Railway. 

### How is sales Tax/VAT handled?

Railway may collect applicable sales tax and VAT on your account based on your billing location and local tax requirements, where and when applicable. When assessed and collected, Sales Tax/VAT is explicitly outlined on your invoice.

To ensure accurate tax assessment, Workspace Admins must verify that their billing information, including Billing Address, Organization Name, and Tax ID (when applicable), is accurate. Organization Name and Tax ID are not required when using Railway for personal use.

To view and manage your subscription, visit the billing section of your workspace.

### How do I remove my saved payment method from my account?

If your subscription is canceled and you have no pending invoices, you can remove your saved payment method by doing the following:

1. Go to the billing page for your workspace
2. Click "Delete" in the payment method section

### What happens if the payment fails for my subscription?

If your subscription payment fails, we retry the payment method on file over several days. We also inform you of the payment failure, in case your payment method needs to be updated.

If payment continues to fail, we flag your services to be stopped and send you a warning.

If we do not receive payment, your services are stopped until all open invoices have been paid.

### My services were stopped, what do I do?

Your services may be stopped by Railway for the following reasons, along with their solutions -

- **Usage limits reached:** You've hit your usage limits. Increase your usage limit, remove it entirely, or wait for the usage limit to reset.

- **Trial credits exhausted:** You've run out of trial credits. Consider upgrading to a paid plan to continue using the service.

- **Failed payment:** Your payment method has failed. Update your payment method and pay your outstanding invoice.

- **Unpaid invoice:** You have an outstanding invoice. Pay your outstanding invoice.

Railway will automatically redeploy your services once the underlying issue is resolved, as long as it is resolved within a period of 30 days. After that, you will have to redeploy them manually from the Removed deployment's 3-dot menu.

**Note:** Although Railway will remove your deployment for any of the above reasons, Railway will not remove the volume attached to the service.

### I am a freelancer or represent an agency. How do I manage my billing relationships with my clients?

Create a Pro plan on Railway and add the client to the workspace. If you run into issues when it's time to hand over your workload to your client, you can reach out to us over Central Station.

### Why did I receive another invoice after cancelling my subscription?

You may receive an invoice containing charges for Resource Usage after you cancel your subscription. These are resource usages you have consumed in that billing cycle that we reserve the right to charge you for.

### How do I request a refund?

Please refer to Pricing -> Refunds.

### Requesting an invoice re-issuance

If you encounter "This invoice can no longer be paid on Stripe" error or need
your Tax ID added to a previous invoice, follow the steps below to get an
invoice reissued.

1. Go to your workspace's billing page at https://railway.com/workspace/billing. Ensure you select the correct workspace using the Workspace Switcher in the top left corner.

2. Scroll to **Billing History**. For the invoice you want to reissue, click on the Gear icon next to it and select **Re-issue**.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1747010826/docs/cs-2025-05-12-08.14_3_lrlrz9.png"
alt="Screenshot of invoice options"
layout="intrinsic"
width={507} height={231} quality={100} />

3. Follow the instructions in the pop-up:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1747010832/docs/cs-2025-05-12-08.14_fyi63w.png"
alt="Screenshot of invoice re-issuance"
layout="intrinsic"
width={876} height={557} quality={100} />

Before you re-issue an invoice, please ensure your billing information is up-to-date.

Once your invoice has been re-issued, it will contain the latest billing
information, and appear in your **Billing History**.

If you do not receive the re-issued invoice within 24 hours, please reach
out to us at station.railway.com.


# Refunds
Source: https://docs.railway.com/pricing/refunds

Learn about Railwayâs refund policy and how to request a refund if eligible.



## Requesting a refund

You can request for a refund in Workspace Settings -> Billing under **Billing History**:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743469117/refund_e0pzvw.png"
alt="Screenshot of refund request button inside Account -> Billing"
layout="intrinsic"
width={1200} height={289} quality={100} />

If you do not see a refund button next to your invoice, you are ineligible for a refund. **This decision is final** and we are unable to issue refunds for invoices that have been deemed ineligible.

After a refund is issued,

- It may take up to 5~10 business days for the refund to be processed and reflected in your account
- Your subscription may be cancelled immediately by us
- Your services may be taken offline immediately

If you'd like to stop using Railway, please remove your projects and cancel your subscription immediately. See "How do I view/manage/cancel my subscription?" for further information.

## FAQs

### Why was my refund request denied?

Refunds are issued at Railway's sole discretion. If your refund request was denied, it may be due to one of the following reasons:

- Your invoice contains resource usage costs. We generally do not issue refunds for resource usage, as those were resources you have consumed (in a manner akin to how a utility company charges for electricity or water)

- You have received a refund from Railway in the past

- You have violated Railway's Fair Use Policy and/or Terms of Service


# Cost control
Source: https://docs.railway.com/pricing/cost-control

Optimize your Railway projects for budget-friendly billing by setting limits and activating serverless.



## Usage limits

Usage Limits allow you to set a maximum limit on your usage for a billing cycle. If your resource usage for the billing cycle exceeds the limit you configured, we will shut down your workloads to prevent them from incurring further resource usage.

### Configuring usage limits

<Image src="https://res.cloudinary.com/railway/image/upload/v1743193518/docs/usage-limits_pqlot9.png" alt="Usage Limits Modal" layout="responsive" width={1200} height={1075} />

Visit the <a href="https://railway.com/workspace/usage" target="_blank">Workspace Usage page</a> to set the usage limits. Once you click the <kbd>Set Usage Limits</kbd> button, you will see a modal where you can set a <kbd>Custom email alert</kbd> and a <kbd>Hard limit</kbd>.

<Banner variant="info">The link above takes you to the usage page for your personal account. If you want to set a usage limit for your workspace, you can use the account switcher in the top left corner of your dashboard to access the workspace's usage page. You must be a workspace admin to configure usage limits.</Banner>

### Custom email alert

You can think of this as a _soft limit_. When your resource usage reaches the specified amount, we will email you that this threshold has been met. Your resources will remain unaffected.

### Hard limit

Once your resource usage hits the specified hard limit, all your workloads will be taken offline to prevent them from incurring further resource usage. Think of the hard limit as the absolute maximum amount you're willing to spend on your infrastructure.

We will send you multiple reminders as your usage approaches your hard limit:

1. When your usage reaches 75% of your hard limit
2. When your usage reaches 90% of your hard limit
3. When your usage reaches 100% of your hard limit and workloads have been taken down.

<Banner variant="danger">Setting a hard limit is a possibly destructive action as you're risking having all your resources shut down once your usage crosses the specified amount.</Banner>

### Usage limits FAQ

<Collapse title="Can I set a usage limit?">
Yes, usage limits are available for all subscription plans.
</Collapse>

<Collapse title="Do I need to set a hard limit to set a custom email alert?">
No. You can leave the hard limit blank if you simply want to be notified at a particular amount of usage.
</Collapse>

<Collapse title="What is the minimum hard limit?">
The minimum amount you can specify as the hard limit is $10.
</Collapse>

<Collapse title="How can I restart my resources if I hit my usage limit?">
To restart your resources, increase your usage limit or remove it entirely. Railway will automatically redeploy your stopped services once the limit is raised or removed. If automatic recovery fails for any service, you can manually redeploy from the deployment's 3-dot menu.
</Collapse>

<Collapse title="Will my resources be automatically started during the next billing cycle?">
Railway will try to automatically restart your resources during the next billing cycle, but if automatic recovery fails for any service, you can manually redeploy from the deployment's 3-dot menu.
</Collapse>

## Resource limits

Resource limits allow you to limit the maximum amount of CPU and memory available to a service.

To configure resource limits, navigate to your service's settings > Deploy > Resource Limits.

<Image
  src="https://res.cloudinary.com/railway/image/upload/v1721917970/resource-limits.png"
  alt="Resource Limits setting"
  layout="intrinsic"
  width={1298}
  height={658}
  quality={80}
/>

<Banner variant="warning">
Setting resource limits too low will cause your service to crash.
</Banner>

Using resource limits makes sense in scenarios where:

1. You don't want to risk a high bill due to unexpected spikes in usage
2. You are okay with the service crashing if it exceeds the limit

## Use private networking

Using Private Networking when communicating with other services (such as databases) within your Railway project will help you avoid unnecessary Network Egress costs.

### With databases

Communicate with your Railway database over private networking by using the DATABASE_URL environment variable, instead of DATABASE_PUBLIC_URL.

### With other services

If your Railway services need to communicate with each other, you can find the service's private URL in the service settings:

<Image src="https://res.cloudinary.com/railway/image/upload/v1743193518/docs/private-networking_nycfyk.png" alt="Private Network URL" layout="responsive" width={1558} height={1156} />

Learn more about Railway's Private Networking here.

## Enabling serverless

Enabling Serverless on a service tells Railway to stop a service when it is inactive, effectively reducing the overall cost to run it.

To enable Serverless, toggle the feature on within the service configuration pane in your project:

<Image src="https://res.cloudinary.com/railway/image/upload/v1696548703/docs/scale-to-zero/appSleep_ksaewp.png"
alt="Enable App Sleep"
layout="intrinsic"
width={700} height={460} quality={100} />

1. Navigate to your service's settings > Deploy > Serverless
2. Toggle "Enable Serverless"
3. To _disable_ Serverless, toggle the setting again

Read more about how Serverless works in the Serverless page.


# Committed spend
Source: https://docs.railway.com/pricing/committed-spend

Learn about Railway's committed spend tier system.



## Available tiers

| Committed spend tier | Features                                                                             |
| -------------------- | ------------------------------------------------------------------------------------ |
| $1000                | 90-day log history, HIPAA BAAs                                                       |
| $2000                | Single Sign-On, Role-based access control, 18 month Audit Logs retention             |
| $5000                | Slack Connect channels,  Critical level support tickets, Railway owned cloud regions |
| $10000               | Dedicated instances, Bring your own cloud                                            |

## How to subscribe

These tiers can only be accessed from a workspace on the Pro plan. To access a committed spend tier:

1. Upgrade your workspace to the Pro plan if you haven't already.
2. Navigate to your workspace Settings -> Plans page.
3. Scroll down to see Committed Spend and Enterprise tier options.

<Image src="https://res.cloudinary.com/railway/image/upload/v1772655571/docs/committed_spend_from_pro_qfa6uc.png"
alt="Committed spend on the pro plan"
layout="intrinsic"
width={800} height={468} quality={100} />

## Feature definitions

### 90-day log history
Extended log retention for better historical analysis and auditing.

### HIPAA BAAs
HIPAA Business Associate Agreements for compliant health data handling. Requires a year commitment paid monthly.

### Single sign-on
Allow workspace members to sign in using your organizationâs Identity Provider (IdP), including Okta, Auth0, Microsoft Entra ID, Google Workspace, and more.

### Role-based access control
Restrict access to sensitive environments like production. Only workspace admins can access restricted environments.

### 18 month audit logs retention
Extended log retention for better historical analysis and auditing.

### Slack Connect channels
A private channel with the solutions team at Railway on Slack to facilitate better communication and support.

### Critical level support tickets
Critical tickets allow you to page our support on-call directly for an immediate response.

### Railway owned cloud regions
Deploy to AWS and GCP via Railway for better availability zone selection.

### Dedicated instances
Custom dedicated infrastructure for enhanced performance and control.

### Bring your own cloud
Deploy Railway within your VPC for ultimate compliance within your infrastructure.

## FAQs

### What happens if my usage is less than the committed spend tier I am subscribed to?

We will add a line item to your invoice to make up for the difference and you will be billed the price of the committed spend tier you are on.
For example: If you're subscribed to the $2000 tier and your usage is $1400, we will add a $600 line item making your bill $2000.

### How do I cancel my committed spend tier subscription?

You can cancel your commitment by going to your workspace billing page. Note: You will immediately lose access to the features attached to the tier upon cancelation.

### My question isn't answered here, where can I speak to the team?
To learn more about committed spend tiers, please contact our team.


# AWS Marketplace
Source: https://docs.railway.com/pricing/aws-marketplace

Learn about Railway's AWS Marketplace offering and pricing.



## Offering

Railway offers solutions, peering templates and deployment to AWS- while using your AWS vendor relationship. For large Enterprises, Railway can be an option for large engineering teams to significantly reduce operational overhead.

## Pricing structure

Pricing for Railway through AWS Marketplace is based on contract duration. You can pay upfront or in installments according to your contract terms with the vendor. The contract includes:

- A specified quantity of usage for the contract duration
- Usage-based pricing for any usage exceeding the entitled amount
- Additional charges applied on top of the contract price for overages

## Contract terms

### 12-month contract

The standard offering is a 12-month contract with the following terms:

- Base price: $10,000.00 per 12 months
- Overage rate: $1.00 per unit
- Private pricing agreements available through the Railway sales team

## Refund policy

All fees are non-refundable and non-cancellable except as required by law.

## Getting started

To purchase Railway through AWS Marketplace:

1. Visit the Railway listing on AWS Marketplace
2. Click "View purchase options"
3. Contact the Railway sales team
4. Complete the purchase through your AWS account

## Support

For questions about AWS Marketplace purchases or to discuss private pricing agreements, please contact the Railway sales team.


# Credits
Source: https://docs.railway.com/pricing/credits

Learn how credits apply to your Railway account if part of a promotion.



## Eligibility

Credits and promotions only apply to new signups. If you already have an account, or signed up before navigating to the unique promotion link, the credits will not apply to you.

## Activating Your Credits

To activate your credits:

1. Sign up for Railway using the unique link provided to you.
2. Navigate to the Plans page to upgrade your plan to Hobby. On the page, you will see the name of your promotion if it applies to your account. For more information on available plans, see the Pricing Plans docs.

<Image src="https://res.cloudinary.com/railway/image/upload/v1772038568/docs/promotion_plans_sftlji.png"
alt="Promotion name on plans page"
layout="intrinsic"
width={800} height={468} quality={100} />

3. Enter your credit card details. A credit card is required to cover any usage that exceeds your credit amount.

You will see the credits applied to your next invoice.

## Viewing Your Credits

Once you have upgraded, you can view your credit and promotion details by navigating to Workspace Settings > Billing. There you will find:

- Whether a promotion code applies to your account
- The credit value and duration of the promotion

<Image src="https://res.cloudinary.com/railway/image/upload/v1772038568/docs/promotion_billing_xwgg9z.png"
alt="Promotion details on billing page"
layout="intrinsic"
width={800} height={468} quality={100} />



# Enterprise
Source: https://docs.railway.com/enterprise

# Compliance
Source: https://docs.railway.com/enterprise/compliance

Learn about Railway's compliance standards and how we ensure security and regulatory adherence.

Companies choose Railway so that they can speed up their development velocity while also maintaining their security and compliance posture.

We are happy to sign NDAs with your company to provide additional information about Railway's security and compliance practices. Please reach out to us at team@railway.com to get started, or click here to book some time to chat.

You can request to view Railway's audit, compliance, security, and regulatory documents and processes on the Trust Center at trust.railway.com.

Additionally, the Railway enterprise plan is the most secure and compliant option. Read about the Railway enterprise plan here.

## Certifications

We know that your businesses need to develop strong and lasting relationships with your vendors to build confidence that we can be trusted to deliver your workloads. Part of that is through certifications, audits, and continual refinement of Railway's practices. Railway aims to comply with all the distributions of workloads and privacy procedures.

### SOC 2 type ii and SOC 3

Railway is SOC 2 Type II certified and SOC 3 certified.

Customers who are in the process of securing SOC 2 certification can request a copy of the Railway security audit on the Trust Center.

### HIPAA BAA

Railway follows a shared responsibility model for HIPAA compliance and PHI. Railway will make its best effort to advise your company on setting up encryption for your data, auditing the storage of keys, establishing access control, and ensuring secure storage of sensitive patient data. When a BAA is in effect, the Railway team will no longer be able to directly access your running workloads.

HIPAA BAA is an add-on with a paid monthly spend threshold. All pricing goes towards your usage on Railway. Monthly thresholds for addons is found in the committed spend pricing.

If your company needs a BAA, you can contact the Railway solutions team at team@railway.com, or click here to schedule some time to chat.

## Privacy

Railway is committed to protecting the privacy of Railway's users. We understand that when working with user code and data, it is important to have a clear understanding of how we handle your data. Railway, on behalf of Railway's users, may remove offending workloads but at no point will a Railway team member modify your application without your expressed permission through an approved communication channel.

Click here to see Railway's Privacy Policy.

## GDPR compliance - data processing agreement (DPA)

Railway provides a Data Processing Agreement (DPA) to help customers comply with GDPR requirements when processing personal data through the Railway platform. If you operate a business in the EU or process personal data of EU residents, you may need to execute a DPA with Railway to ensure compliance with GDPR Article 28 requirements for data processor relationships.

You can access and execute Railway's standard DPA through the self-service link: Sign Railway's DPA

You can also review Railway's standard DPA terms at railway.com/legal/dpa.

## VAT tax ID and address

Customers in the EU may need to add their VAT Tax ID to their invoices for compliance and reporting purposes.

You can add your VAT Tax ID and address on Railway in your Workspace settings -> Billing -> Manage Subscription.

If you have multiple workspaces, you need to add your VAT Tax information to each respective Workspace's Subscription.

After adding your information, it will appear on your future invoices.

## EU DORA

For European organizations in finance that need to comply with EU Dora - Railway is willing to provide documents after a click through NDA that describe disaster recovery procedures, uptime statistics, and IT controls for organizations to who need to submit compliance documents to local regulators. You can get information on the Trust Page

## Deploy securely on Railway

If compliance is top of mind, the Railway enterprise plan will meet your needs. From product features like SSO, to higher capacity limits, to security audits, the Railway enterprise plan is made to satisfy even the largest organizations. Read more about the Railway enterprise plan.


# Audit logs
Source: https://docs.railway.com/enterprise/audit-logs

Learn more about how Railway keeps a record of actions in workspaces.

Audit logs can be accessed by workspace admins through the <a href="https://railway.com/workspace/audit-logs" target="_blank">**Audit Logs**</a> link in the workspace settings.

Audit logs help teams with:

- **Security:** Track who made changes to sensitive resources like environment variables, integrations, or workspace settings
- **Compliance:** Maintain records of all changes for regulatory requirements and internal policies
- **Troubleshooting:** Identify when and how changes were made to diagnose issues
- **Team Coordination:** Understand what changes team members are making across projects
- **Change Management:** Review the history of deployments and configuration changes

<Image src="https://res.cloudinary.com/railway/image/upload/v1743471483/docs/audit-logs-list_ryluzl.png"
alt="Screenshot of audit log list"
layout="responsive"
width={1652} height={1538} quality={80} />

## Accessing audit logs

Audit logs are available at the workspace level and can be accessed by workspace admins through the workspace settings page.

To view audit logs:
1. Navigate to your workspace dashboard
2. Click on <a href="https://railway.com/workspace/audit-logs" target="_blank">**Audit Logs**</a> in the sidebar

For more information about workspace roles and permissions, see the Workspaces documentation.

## Log contents

Each audit log entry contains detailed information about the action that was performed:

- **Event Type:** The type of action that occurred (e.g., service created, variable updated, deployment triggered)
- **Timestamp:** When the action was performed
- **Workspace:** The workspace where the action occurred
- **Project:** The project affected by the action (if applicable)
- **Environment:** The environment affected by the action (if applicable)
- **Event Data:** Specific details about the change, such as resource data that was created, modified, or deleted
- **Actor:** Information about who or what performed the action

<Image src="https://res.cloudinary.com/railway/image/upload/v1743471483/docs/audit-log-details_e1wipe.png"
alt="Screenshot of audit log details"
layout="responsive"
width={1559} height={1339} quality={80} />

### Actor types

Actions in audit logs can be performed by three types of actors:

- **User:** An action performed by a workspace or project member
- **Railway Staff:** An action performed by Railway's team (typically during support requests)
- **Railway System:** An automated action performed by Railway's platform (e.g., automatic updates, backups)

<Banner variant="info">
Historic events from before audit logs were released may not contain information about the actor.
</Banner>

## Listing all audit logs event types

The complete documentation of all audit log event types and their descriptions can be retrieved using the Railway GraphQL API.

You can explore this information using the <a href="https://railway.com/graphiql" target="_blank">GraphiQL playground</a>:

This query returns all available event types in audit logs, along with a description of what each event represents.

## Exporting audit logs via the API

You can export audit logs programmatically using the Railway GraphQL API.

Use the auditLogs query to retrieve audit log entries for a specific workspace. You can test this query in the <a href="https://railway.com/graphiql" target="_blank">GraphiQL playground</a>:

For more information on using the GraphQL API, see the Public API Guide.

## Audit log retention

Audit logs are retained for different periods depending on your Railway plan:

| Plan                       | Retention Period |
| -------------------------- | ---------------- |
| **Free, Trial and Hobby**  | 48 hours         |
| **Pro**                    | 30 days          |
| **Enterprise**             | 18 months        |

For longer retention periods or custom log export solutions, consider upgrading to a higher plan or contact us to discuss Enterprise options.

## Code Examples

{
  auditLogEventTypeInfo {
    eventType
    description
  }
}

{
  auditLogs(workspaceId: "YOUR_WORKSPACE_ID") {
    edges {
      node {
        id
        eventType
        createdAt
        projectId
        environmentId
        payload
        context
      }
    }
    pageInfo {
      endCursor
      hasNextPage
      hasPreviousPage
      startCursor
    }
  }
}


# SAML SSO
Source: https://docs.railway.com/enterprise/saml

Learn about how to configure and use SAML Single Sign-On (SSO) for your Railway workspace.

SAML SSO is available on Railway Enterprise.
</Banner>

**SAML Single Sign-On (SSO)** allows workspace members to sign in using your organizationâs Identity Provider (IdP), including Okta, Auth0, Microsoft Entra ID, Google Workspace, and more.

New users signing in with your Identity Provider are automatically added to your workspace as workspace members.

## Configuring SAML SSO

<Image src="https://res.cloudinary.com/railway/image/upload/v1743471483/docs/saml-and-trusted-domains_snwbkn.png"
alt="Screenshot of SAML Settings and Trusted Domains"
layout="responsive"
width={1620} height={1586} quality={80} />

To configure SAML SSO, go to your workspaceâs <a href="https://railway.com/workspace/people" target="_blank">People settings</a>. You must be a workspace admin with access to your Identity Providerâs configuration panel.

1. Add your organizationâs email domain(s) as **Trusted Domains**.
2. In the **SAML Single Sign-On** section, click **Configure** and follow the guided setup to connect your Identity Provider to Railway.
3. Optionally, enforce SAML SSO to require members to log in through your Identity Provider.

Once configured, users can login using SAML SSO using their organization email. Existing users must update their Railway email if it differs from their Identity Provider email.

_If youâre a Railway Enterprise customer and donât see the SAML settings in your workspace, please contact us._

## Enforcing SAML SSO

<Image src="https://res.cloudinary.com/railway/image/upload/v1743471483/docs/saml-enforcement_zgg55p.png"
alt="Screenshot of enforcing SAML SSO in a workspace"
layout="responsive"
width={1624} height={886} quality={80} />

Workspace admins can **enforce SAML SSO** to ensure all members access the workspace with your Identity Provider.

- **Enable enforcement** by toggling "Members need to login with SAML SSO."
- Only workspace admins already logged in with SAML SSO can enable enforcement.
- When enforcement is active, users not authenticated with SAML SSO canât open the workspace or access its resources.
- Enforcement takes effect immediately. Active users without SAML authentication will be prompted to re-authenticate.

Note: Enforcement will not limit which login methods a user can use. Because Railway users can be members of multiple workspaces, they can still log in with other methods, but must use SAML SSO to access the SAML-enforced workspace.

<video src="https://res.cloudinary.com/railway/video/upload/v1753470547/docs/saml-enforcement-demo_upg3hq.mp4" controls autoPlay loop muted style={{ borderRadius: 10 }}></video>

## Login using SSO

After SAML SSO is enabled, users can log in using their organizationâs email by selecting _"Log in using Email"_ â _"Log in using SSO"_.

Alternatively, go directly to https://railway.com/login#login-saml.

Railway also supports IdP-initiated SSO, allowing users to access Railway directly from their Identity Providerâs dashboard.

## Supported identity providers

We support all identity providers that use **SAML** or **OIDC**, including:

- Okta
- Microsoft Entra ID (Azure AD)
- Auth0
- Google
- JumpCloud
- ADP
- CAS
- ClassLink
- Cloudflare
- Ping Identity
- CyberArk
- Duo
- Keycloak
- LastPass
- Login.gov
- miniOrange
- NetIQ
- OneLogin
- Oracle
- Rippling
- Salesforce
- Shibboleth
- SimpleSAMLphp
- VMware Workspace

and any other provider compatible with **SAML** or **OIDC**.

## SSO-related events

You can receive notifications when important SSO-related events were triggered:

- **SSO Connected:** when an Identity Provider is successfully connected to the workspace.
- **SSO Disconnected:** when the Identity Provider is disconnected from the workspace.
- **SSO Updated:** when SAML enforcement is enabled or disabled.
- **SAML Certificate requires renewal:** when the SAML certificate is nearing expiration or has expired. This event is triggered multiple times before and after expiration.
- **SAML Certificate renewed:** when the SAML certificate is successfully renewed.


# Environment RBAC
Source: https://docs.railway.com/enterprise/environment-rbac

Restrict access to sensitive environments like production with role-based access control.

Environment RBAC is available on Railway Enterprise.
</Banner>

Environment RBAC (Role-Based Access Control) allows you to restrict access to sensitive environments like production. This ensures that only authorized team members can view or modify critical infrastructure.

## How it works

When an environment is marked as restricted:

- **Non-admin members** can see that the environment exists but cannot access its resources
- **Restricted resources** include variables, logs, metrics, services, and configurations
- **Deployments** can still be triggered via git push, allowing developers to deploy without accessing sensitive data

This separation allows development teams to deploy code while keeping production secrets and configurations secure.

## Enabling environment RBAC

Subscribe to a committed spend plan to enable RBAC.

Once enabled for your workspace:

1. Go to **Project Settings â Environments**
2. Find the environment you want to restrict (e.g., production)
3. Toggle the **Restricted** switch

<Image
  src="https://res.cloudinary.com/railway/image/upload/v1764189412/CleanShot_2025-11-26_at_17.33.18_2x_xzaztj.png"
  alt="Restricted environments toggle in Project Settings"
  layout="responsive"
  width={817}
  height={528}
  quality={80}
/>

## Role permissions

| Role | Can access restricted environments | Can toggle restriction |
| :--- | :---: | :---: |
| Admin | âï¸ | âï¸ |
| Member | â | â |
| Deployer | â | â |

### Admin

Admins have full access to all environments, including restricted ones. They can:
- View and modify variables, services, and configurations
- Access logs and metrics
- Toggle the restricted status on any environment

### Member

Members cannot access restricted environments. They can:
- See that the environment exists in the project
- Trigger deployments via git push
- Access non-restricted environments normally

### Deployer

Deployers have the same restrictions as Members for restricted environments. They can:
- Trigger deployments via git push
- Cannot view variables, logs, or configurations in restricted environments

## Use cases

### Protecting production secrets

Keep production API keys, database credentials, and third-party service tokens hidden from developers who don't need access.

### Compliance requirements

Meet security compliance requirements (SOC 2, HIPAA, etc.) by limiting access to production data and configurations.

### Separation of duties

Allow developers to deploy code without having access to view or modify production infrastructure settings.

## Best practices

1. **Restrict production by default** - Mark your production environment as restricted immediately after enabling the feature
2. **Limit admin count** - Only grant admin access to team members who need to manage production configurations
3. **Use staging for debugging** - Keep a non-restricted staging environment that mirrors production for debugging purposes
4. **Audit regularly** - Review who has admin access periodically to ensure it aligns with current team responsibilities

## Related

- Environments - Learn about environment management
- Project Members - Manage team access and roles
- Enterprise Features - Explore other enterprise capabilities



# AI
Source: https://docs.railway.com/ai

# Agent skills
Source: https://docs.railway.com/ai/agent-skills

Agent skills for interacting with Railway directly from your AI coding assistant.



## What are agent skills?

Agent Skills are an open format for extending AI coding assistants with specialized knowledge and capabilities. They follow the Agent Skills specification.

Skills are markdown files (SKILL.md) that contain:
- **Metadata** in YAML frontmatter
- **Instructions** with step-by-step guidance for the AI agent
- **Examples** showing expected behavior

When you ask your AI assistant something like "deploy to Railway" or "check my project status," the agent automatically selects the appropriate skill based on your intent and follows its instructions.

### Supported tools

- <a href="https://claude.ai/code" target="_blank">Claude Code</a>
- <a href="https://openai.com/codex" target="_blank">OpenAI Codex</a>
- <a href="https://opencode.ai" target="_blank">OpenCode</a>
- <a href="https://cursor.com" target="_blank">Cursor</a>

## Installation

You can also install via <a href="https://skills.sh" target="_blank">skills.sh</a>:

Supports Claude Code, OpenAI Codex, OpenCode, and Cursor. Re-run to update.

**Note:** For Claude Code, you can also install through the Claude Code plugin marketplace.

## The use-railway skill

The repository ships one skill called use-railway. It uses a route-first design where intent routing is defined in the skill file and execution details are split into action-oriented references.

### Workflow coverage

The use-railway skill covers the following areas:

- **Project and service setup** - Create projects, add services, scaffold code for deployment, and link existing projects
- **Deploy and release operations** - Push code to Railway, manage deployments, and handle the deployment lifecycle
- **Troubleshooting and recovery** - View build and deploy logs, redeploy, restart, or remove deployments
- **Environment config and variables** - Query and modify service configuration, environment variables, build/deploy commands, replicas, health checks, and restart policies
- **Bucket management** - Create, list, inspect, rename, and delete storage buckets, and view or reset S3-compatible credentials
- **Networking and domains** - Add Railway-provided domains, configure custom domains, and manage domain settings
- **Status and observability** - Check project status, query resource usage metrics (CPU, memory, network, disk), and monitor services
- **Projects and workspaces** - List projects, switch between projects, and manage project settings
- **Docs and community search** - Fetch Railway documentation and search Central Station for community threads and discussions

## Source

The Railway agent skills are open-source and available on <a href="https://github.com/railwayapp/railway-skills" target="_blank">GitHub</a>.

## Code Examples

curl -fsSL railway.com/skills.sh | bash

npx skills add railwayapp/railway-skills


# Claude Code plugin
Source: https://docs.railway.com/ai/claude-code-plugin

Install the Railway plugin for Claude Code to manage your infrastructure with natural language.

The plugin is distributed through Claude Code's plugin marketplace system and installs the use-railway agent skill along with supporting scripts and hooks.

## Prerequisites

- <a href="https://claude.ai/code" target="_blank">Claude Code</a> installed (version 1.0.33 or later)
- The Railway CLI installed and authenticated

## Installation

<Steps>
  <Step title="Add the Railway marketplace">
    From within Claude Code, add the Railway plugin marketplace:

    This registers the Railway marketplace and makes the plugin available to install.
  </Step>
  <Step title="Install the plugin">
    Install the Railway plugin from the marketplace:

    You can also browse and install through the interactive plugin manager by running /plugin and navigating to the **Discover** tab.
  </Step>
</Steps>

After installation, the plugin's skills are available in your Claude Code session. Ask your assistant to deploy services, check project status, manage environments, or perform any of the tasks covered by the use-railway skill.

## Update the plugin

To update to the latest version, refresh the marketplace and reinstall:

You can also enable auto-updates for the marketplace through the /plugin interface under the **Marketplaces** tab.

## What's included

The plugin installs the following components:

- **use-railway skill** - A route-first agent skill that covers project setup, deployments, troubleshooting, environment configuration, networking, observability, and more. See Agent Skills for the full list of capabilities. The skill includes action-oriented reference documents and a GraphQL API helper script for authenticated Railway API requests.
- **Auto-approve hook** - A PreToolUse hook that automatically approves Railway CLI commands and Railway API script calls, so Claude Code doesn't prompt for permission on every Railway operation.

## Alternative installation

If you prefer to install the agent skill without the Claude Code plugin system, you can use the general-purpose installer that works across multiple AI coding assistants:

See Agent Skills for more details.

## Source

The Railway Claude Code plugin is open-source and available on <a href="https://github.com/railwayapp/railway-skills" target="_blank">GitHub</a>.

## Code Examples

/plugin marketplace add railwayapp/railway-skills

/plugin install railway@railway-skills

/plugin marketplace update railway-skills

curl -fsSL railway.com/skills.sh | bash


# MCP server
Source: https://docs.railway.com/ai/mcp-server

Learn about the official Railway MCP (Model Context Protocol) server and how to use it.

With this server, you can ask your IDE or AI assistant to create projects, deploy templates, create/select environments, or pull environment variables.

The Railway MCP Server is open-source and available on GitHub.

## Understanding MCP and Railway MCP server

The **Model Context Protocol (MCP)** defines a standard for how AI applications (hosts) can interact with external tools and data sources through a client-server architecture.

* **Hosts**: Applications such as Cursor, VS Code, Claude Desktop, or Windsurf that connect to MCP servers.
* **Clients**: The layer within hosts that maintains one-to-one connections with individual MCP servers.
* **Servers**: Standalone programs (like the Railway MCP Server) that expose tools and workflows for managing external systems.

The **Railway MCP Server** acts as the server in this architecture, translating natural language requests into CLI workflows powered by the Railway CLI.

## Prerequisites

To get started with the MCP server, you need to have the Railway CLI installed and authenticated.

## Installation

### Cursor

You can one-click install the MCP server in Cursor by clicking the "Add to Cursor" button below:

![Install MCP Server](https://cursor.com/en/install-mcp?name=Railway&config=eyJjb21tYW5kIjoibnB4IC15IEByYWlsd2F5L21jcC1zZXJ2ZXIifQ%3D%3D)

Alternatively, you can add the following configuration to your .cursor/mcp.json file manually:

### VS Code

Add the following configuration to your .vscode/mcp.json file:


### Claude Code

To install the MCP server in Claude Code, you can use the following command:

## Example usage

* **Create and deploy a new app**

* **Deploy from a template**

* **Pull environment variables**

* **Create a new environment**

## Available MCP tools

The Railway MCP Server provides a curated set of tools. Your AI assistant will automatically call these tools based on the context of your request.

* **Status**

  * check-railway-status - Verify CLI installation and authentication

* **Project Management**

  * list-projects - List all projects
  * create-project-and-link - Create a project and link it to the current directory

* **Service Management**

  * list-services - List project services
  * link-service - Link a service to the current directory
  * deploy - Deploy a service
  * deploy-template - Deploy from the Railway Template Library

* **Environment Management**

  * create-environment - Create a new environment
  * link-environment - Link environment to current directory

* **Configuration & Variables**

  * list-variables - List environment variables
  * set-variables - Set environment variables
  * generate-domain - Generate a Railway domain

* **Monitoring & Logs**

  * get-logs - Retrieve service logs

## Security considerations

Under the hood, the Railway MCP Server runs the Railway CLI commands. While destructive operations are intentionally excluded and not exposed as MCP tools, you should still:

* **Review actions** requested by the LLM before running them.
* **Restrict access** to ensure only trusted users can invoke the MCP server.
* **Avoid production risks** by limiting usage to local development and non-critical environments.

## Feature requests

The Railway MCP Server is a work in progress. We are actively working on adding more tools and features. If you have a feature request, leave your feedback on this Central Station post.

## Code Examples

{
  "mcpServers": {
    "Railway": {
      "command": "npx",
      "args": ["-y", "@railway/mcp-server"]
    }
  }
}

{
  "servers": {
    "Railway": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@railway/mcp-server"]
    }
  }
}

claude mcp add Railway npx @railway/mcp-server

Create a Next.js app in this directory and deploy it to Railway.
  Also assign it a domain.

Deploy a Postgres database

Deploy a single node ClickHouse database

Pull environment variables for my project and save them to a .env file

Create a development environment called `development` 
  cloned from production and set it as linked



# Templates & open source
Source: https://docs.railway.com/templates & open source

# Deploy
Source: https://docs.railway.com/templates/deploy

Learn how to deploy Railway templates.

connected to infrastructure.

You can find featured templates on the <a href="https://railway.com/templates" target="_blank">template marketplace</a>.

## Template deployment flow

To deploy a template -

- Find a template from the marketplace and click Deploy Now
- If necessary, configure the required variables, and click Deploy
- Upon deploy, you will be taken to your new project containing the template service(s)
  - Services are deployed directly from the defined source in the template configuration
  - After deploy, you can find the service source by going to the service's settings tab
  - Should you need to make changes to the source code, you will need to eject from the template repo to create your own copy. See next section for more detail.

_Note: You can also deploy templates into existing projects, by clicking + New from your project canvas and selecting Template._

## Getting help with a template

If you need help with a template you have deployed, you can ask the template creator directly:

1. Find the template page in the marketplace
2. Click **"Discuss this Template"** on the template details page
3. Your question will be posted to the template's queue where the creator can help

Template creators are notified when questions are posted and are incentivized to provide helpful responses through Railway's kickback program.

<Image src="https://res.cloudinary.com/railway/image/upload/v1764639364/Ask_the_Template_Creator_wwzlca.png" alt = "Ask the Template Creator" width={1538} height={1618} quality={100} />

## Eject from template repository

<Banner variant="info">
As of March 2024, the default behavior for deploying templates, is to attach to and deploy directly from the template repository.  Therefore, you will not automatically get a copy of the repository on deploy.  Follow the steps below to create a repository for yourself.
</Banner>

By default, services deployed from a template are attached to and deployed directly from the template repository. In some cases, you may want to have your own copy of the template repository.

Follow these steps to eject from the template repository and create a mirror in your own GitHub account.

1. In the service settings, under Source, find the **Upstream Repo** setting
2. Click the Eject button
3. Select the appropriate GitHub organization to create the new repository
4. Click Eject service

## Updatable templates

When you deploy any services from a template based on a GitHub repo, every time you visit the project in Railway, we will check to see if the project it is based on has been updated by its creator.

If it has received an upstream update, we will create a branch on the GitHub repo that was created when deploying the template, allowing for you to test it out within a PR deploy.

If you are happy with the changes, you can merge the pull request, and we will automatically deploy it to your production environment.

If you're curious, you can read more about how we built updatable templates in this <a href="https://blog.railway.com/p/updatable-starters" target="_blank">blog post</a>

_Note: This feature only works for services based on GitHub repositories. At this time, we do not have a mechanism to check for updates to Docker images from which services may be sourced._


# Create
Source: https://docs.railway.com/templates/create

Learn how to create reusable templates on Railway to enable effortless one-click deploys.

By defining services, environment configuration, network settings, etc., you lay the foundation for others to deploy the same software stack with the click of a button.

If you publish your template to the <a href="https://railway.com/templates" target="_blank">marketplace</a>, you can earn kickbacks from usage, up to 25% for open source templates with active community support. Learn more about the kickback program.

## How to create a template

You can either create a template from scratch or base it off of an existing project.

### Starting from scratch

To create a template from scratch, head over to your <a href="https://railway.com/workspace/templates" target="_blank">Templates</a> page within your workspace settings and click on the New Template button.

- Add a service by clicking the Add New button in the top right-hand corner, or through the command palette (CMD + K -> + New Service)
- Select the service source (GitHub repo or Docker Image)
- Configure the service variables and settings

  <Image src="https://res.cloudinary.com/railway/image/upload/v1715724184/docs/templates-v2/composer_aix1x8.gif"
  alt="Template Editor"
  layout="intrinsic"
  width={900} height={1120} quality={80} />

- Once you've added your services, click Create Template
- You will be taken to your templates page where you can copy the template URL to share with others

Note that your template will not be available on the template marketplace, nor will be eligible for a kickback, until you publish it.

### Private repo support

It's now possible to specify a private GitHub repo when creating a template.

This feature is intended for use among Workspaces and Organizations. Users supporting a subscriber base may also find this feature helpful to distribute closed-source code.

To deploy a template that includes a private repo, look for the GitHub panel in the Account Integrations section of General Settings. Then select the Edit Scope option to grant Railway access to the desired private repos.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1721350229/docs/github-private-repo_m46wxu.png"
alt="Create a template from a private GitHub repositories"
layout="intrinsic"
width={1599}
height={899}
quality={80}
/>

If you do not see the Edit Scope option, you may still need to connect GitHub to your Railway account.

### Private Docker images

If your template includes a private Docker image, you can provide your registry credentials without exposing them to users who deploy your template.

To set this up, add a service with a Docker image source in the template editor, then enter your registry credentials in the service settings. Railway encrypts and stores these credentials securely.

When users deploy your template, Railway automatically authenticates with your registry to pull the image. Users will only see that the service uses hidden registry credentials, not the credentials themselves.

<Banner variant="warning">
To protect your credentials, SSH access is disabled and users cannot modify the Docker image source for services with hidden registry credentials.
</Banner>

### Convert a project into a template

You can also convert an existing project into a ready-made Template for other users.

- From your project page, click Settings in the right-hand corner of the canvas
- Scroll down until you see **Generate Template from Project**
- Click Create Template

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743198969/docs/create-template_ml13wy.png"
alt="Generate template from project"
layout="intrinsic"
width={1200}
height={380}
quality={80}
/>

- You will be taken to the template composer page, where you should confirm the settings and finalize the template creation

## Configuring services

Configuring services using the template composer is very similar to building a live project in the canvas.

Once you add a new service and select the source, you can configure the following to enable successful deploys for template users:

- **Variables tab**
  - Add required Variables.
    _Use reference variables where possible for a better quality template_
- **Settings tab**
  - Add a Root Directory (Helpful for monorepos)
  - Enable Public Networking with TCP Proxy or HTTP
  - Set a custom Start command
  - Add a Healthcheck Path
- **Add a volume**
  - To add a volume to a service, right-click on the service, select Attach Volume, and specify the Volume mount path

### Specifying a branch

To specify a particular GitHub branch to deploy, simply enter the full URL to the desired branch in the Source Repo configuration. For example -

- This will deploy the main branch: https://github.com/railwayapp-templates/postgres-ssl
- This will deploy the new branch: https://github.com/railwayapp-templates/postgres-ssl/tree/new

### Template variable functions

Template variable functions allow you to dynamically generate variables (or parts of a variable) on demand when the template is deployed.

<Image src="https://res.cloudinary.com/railway/image/upload/v1743198983/docs/template-variables_dp5pg5.png"
alt="Template Variable Functions"
layout="intrinsic"
width={1200} height={428} quality={100} />

When a template is deployed, all template variable functions are executed and the result replaces the ${{ ... }} in the variable.

Use template variables to generate a random password for a database, or to generate a random string for a secret.

The current template variable functions are:

1. secret(length?: number, alphabet?: string): Generates a random secret (32 chars by default).

   **Tip:** You can generate Hex or Base64 secrets by constructing the appropriate alphabet and length.

   - openssl rand -base64 16 â

   - openssl rand -base64 32 â

   - openssl rand -base64 64 â

     
   - openssl rand -hex 16 â

   - openssl rand -hex 32 â

   - openssl rand -hex 64 â

   Or even generate a UUIDv4 string -

2. randomInt(min?: number, max?: number): Generates a random integer between min and max (defaults to 0 and 100)

## Managing your templates

You can see all of your templates on your <a href="https://railway.com/workspace/templates" target="_blank">Workspace's Template page</a>. Templates are separated into Personal and Published templates.

You can edit, publish/unpublish and delete templates.

<Image src="https://res.cloudinary.com/railway/image/upload/v1743199089/docs/templates_xyphou.png"
 alt="Account templates page"
 layout="intrinsic"
 width={1200}
 height={668}
 quality={80}
/>

## Code Examples

${{secret(22, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/")}}==

${{secret(43, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/")}}=

${{secret(86, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/")}}==

${{secret(32, "abcdef0123456789")}}

${{secret(64, "abcdef0123456789")}}

${{secret(128, "abcdef0123456789")}}

${{secret(8, "0123456789abcdef")}}-${{secret(4, "0123456789abcdef")}}-4${{secret(3, "0123456789abcdef")}}-${{secret(1, "89ab")}}${{secret(3, "0123456789abcdef")}}-${{secret(12, "0123456789abcdef")}}


# Updates
Source: https://docs.railway.com/templates/updates

Learn how template updates work for authors and consumers.



## For template authors

As a template author, you can push updates to all users who have deployed your template. When you merge changes to the root branch (typically main or master) of your template's GitHub repository, Railway will automatically detect these changes and notify users who have deployed your template that an update is available.

Users will receive a notification about the update and can choose to apply it to their deployment when they're ready.

<Banner variant="info">
**Best Practice**: Keep your template's changelog up to date and document breaking changes clearly so that consumers understand what's changing when they receive update notifications.
</Banner>

### Requirements

- Your template must be based on a GitHub repository
- Updates are triggered when changes are merged to the root branch (main or master)
- Docker image-based templates cannot be automatically updated through this mechanism

### Update workflow

1. Make changes to your template's GitHub repository
2. Merge changes to the root branch
3. Railway detects the changes automatically
4. Users who deployed your template receive an update notification
5. Users can choose when to apply the update

## For template consumers

When you deploy any services from a template based on a GitHub repo, Railway will check to see if the template has been updated by its creator.

If an upstream update is available, you will receive a notification. You can then choose to apply the update to your deployment when you're ready.

### How updates work

- Railway monitors the template's source repository for changes
- When updates are detected, you'll see a notification in your project
- Updates are opt-in, you control when to apply them
- Review the template author's changelog before updating to understand what's changing

### Limitations

- This feature only works for services based on GitHub repositories
- At this time, there is no mechanism to check for updates to Docker images from which services may be sourced

<Banner variant="info">
If you're curious, you can read more about how we built updatable templates in this <Link href="https://blog.railway.com/p/updatable-starters" target="_blank">blog post</Link>.
</Banner>


# Best practices
Source: https://docs.railway.com/templates/best-practices

Learn the best practices for template creation.



## Checklist

Depending on the type of template, there are different things to consider:

- Template and Service Icons
- Naming Conventions
- Private Networking
- Environment Variables
- Health Checks
- Persistent Storage
- Authentication
- Dry Code
- Workspace Naming
- Overview

## Template and service icons

Template and service icons are important for branding and recognition, as they give the template a more professional look and feel.

Always use 1:1 aspect ratio icons or logos with transparent backgrounds for both the template itself and the services the template includes.

Transparent backgrounds ensure logos integrate seamlessly with Railway's interface and provide a more polished, professional appearance.

## Naming conventions

Naming conventions are important for readability and consistency; using proper names enhances the overall quality and credibility of your template.

Always follow the naming conventions for the software that the template is made for.

Example, if the template is for ClickHouse, the service and template name should be named ClickHouse with a capital C and H, since that is how the brand name is spelled.

For anything else, such as custom software:

- Use capital case.
- Avoid using special characters or dashes, space-delimited is the way to go.
- Prefer shorter names over longer names for better readability.
- Keep names concise while maintaining clarity.

## Private networking

Private networking provides faster, free communication between services and reduces costs compared to routing traffic through the public internet.

Always configure service-to-service communication (such as backend to database connections) to use private network hostnames rather than public domains.

For more details, see the private networking guide and reference documentation.

## Environment variables

Properly set up environment variables are a great way to increase the usability of your template.

When using environment variables:

- Always include a description of what the variable is for.

- If a variable is optional, include a description explaining its purpose and what to set it to or where to find its value.

- For any secrets, passwords, keys, etc., use template variable functions to generate them, avoid hardcoding default credentials at all costs.

- Use reference variables when possible for dynamic service configuration.

- When referencing a hostname, use the private network hostname rather than the public domain, e.g., RAILWAY_PRIVATE_DOMAIN rather than RAILWAY_PUBLIC_DOMAIN.

- Include helpful pre-built variables that the user may need, such as database connection strings, API keys, hostnames, ports, and so on.

## Health checks

Health checks are important for ensuring that the service is running properly, before traffic is routed to it.

Although a health check might not be needed for all software, such as Discord bots, when it is applicable, it is a good idea to include a health check.

A readiness endpoint is the best option; if that's not possible, then a liveness endpoint should be used.

For more details, see the healthchecks guide and reference documentation.

## Persistent storage

Persistent storage is essential for templates that include databases, file servers, or other stateful services that need to retain data across deployments.

Always include a volume for these services.

Without persistent storage, data will be lost between redeployments, leading to unrecoverable data loss for template users.

When configuring the service, ensure the volume is mounted to the correct path. An incorrect mount path will prevent data from being stored in the volume.

Some examples of software that require persistent storage:

- **Databases:** PostgreSQL, MySQL, MongoDB, etc.
- **File servers:** Nextcloud, ownCloud, etc.
- **Other services:** Redis, RabbitMQ, etc.

The volume mount location depends entirely on where the software expects it to be mounted. Refer to the software's documentation for the correct mount path.

For more details, see the volumes guide and reference documentation.

## Authentication

Authentication is a common feature for many software applications, and it is crucial to properly configure it to prevent unauthorized access.

If the software provides a way to configure authentication, such as a username and password, or an API key, you should always configure it in the template.

For example, ClickHouse can operate without authentication, but authentication should always be configured so as not to leave the database open and unauthenticated to the public.

Passwords, API keys, etc. should be generated using template variable functions, and not hardcoded.

## Dry Code

This is most applicable to templates that deploy from GitHub.

When creating templates that deploy from GitHub, include only the essential files needed for deployment. Avoid unnecessary documentation, example files, or unused code and configurations that don't contribute to the core functionality.

A clean, minimal repository helps users quickly understand the template's structure and make customizations when needed.

## Workspace naming

When users deploy a template, the template author appears as the name of the <a href="/projects/workspaces" target="_blank">workspace</a> that created and published it.

Since the author is publicly visible and shown with the template to the users, it is important to make sure the workspace name is professional and **accurately represents your relationship to the software**.

**Important:** Only use a company or organization name as your workspace name if you are officially authorized to represent that entity. Misrepresenting your affiliation is misleading to users and violates trust.

**If you are officially affiliated** with the software (e.g., you work for ClickHouse and are creating a ClickHouse template), then using the official company name "ClickHouse, Inc." is appropriate and helpful for users to identify official templates.

**If you are not officially affiliated** with the software, always use your own professional name as the workspace name.

**Note:** To transfer a template from one workspace to another, <a href="https://station.railway.com/" target="_blank">contact support</a>.

## Overview

The overview is the first thing users will see when they click on the template, so it is important to make it count.

The overview should include the following:

- **H1: Deploy and Host [X] with Railway**

  What is X? Your description in roughly ~ 50 words.

- **H2: About Hosting [X]**

  Roughly 100 word description what's involved in hosting/deploying X

- **H2: Common Use Cases**

  In 3-5 bullets, what are the most common use cases for [X]?

- **H2: Dependencies for [X] Hosting**

  In bullet form, what other technologies are incorporated in using this template besides [X]?

- **H3: Deployment Dependencies**

  Include any external links relevant to the template.

- **H3: Implementation Details (Optional)**

  Include any code snippets or implementation details. This section is optional. Exclude if nothing to add.

- **H3: Why Deploy [X] on Railway?**

  Railway is a singular platform to deploy your infrastructure stack. Railway will host your infrastructure so you don't have to deal with configuration, while allowing you to vertically and horizontally scale it.

  By deploying [X] on Railway, you are one step closer to supporting a complete full-stack application with minimal burden. Host your servers, databases, AI agents, and more on Railway.


# Publish and share
Source: https://docs.railway.com/templates/publish-and-share

Learn how to publish and share your Railway templates.



## Publishing a template

After you create your template, simply click the publish button and fill out the form to publish your template.

<Image src="https://res.cloudinary.com/railway/image/upload/v1753243835/docs/reference/templates/mockup-1753242978376_skjt7w.png"
  alt="Template publishing form"
  layout="intrinsic"
  width={2004}
  height={3834}
  quality={80}
/>

You can always publish your template by going to the <a href="https://railway.com/workspace/templates" target="_blank">Templates page in your Workspace settings</a> and choose Publish next to the template you'd like to publish.

Optionally, you can add a demo project to your template. This will be used to showcase your template in a working project, and can be accessed by clicking on the Live Demo button in the template's overview page.

## Sharing your templates

After you create your template, you may want to share your work with the public and let others clone your project. You are provided with the Template URL where your template can be found and deployed.

### Deploy on Railway button

To complement your template, we also provide a Deploy on Railway button which you can include in your README or embed it into a website.

<Image src="https://res.cloudinary.com/railway/image/upload/v1676438967/docs/deploy-on-railway-readme_iwcjjw.png" width={714} height={467} alt="Example README with Deploy on Railway button" />

!https://railway.com/button.svg
The button is located at https://railway.com/button.svg.

#### Markdown

To render the button in Markdown, copy the following code and replace the template code with your desired template. If you'd like to help us attribute traffic to your template, replace utm_campaign=generic in the URL with your template name.

#### HTML

To render the button in HTML, copy the following code and replace the template code with your desired template. If you'd like to help us attribute traffic to your template, replace utm_campaign=generic in the URL with your template name.

### Examples

Here are some example templates from the <a href="https://railway.com/templates" target="_blank">template marketplace</a> in button form:
|Icon|Template|Button|
|:--:|:------:|:----:|
|<img src="https://devicons.railway.com/i/nodejs.svg" alt="Node" width="25" height="25" />|Node|![Deploy on Railway](https://railway.com/new/template/ZweBXA?utm_medium=integration&utm_source=button&utm_campaign=node)|
|<img src="https://devicons.railway.com/i/deno.svg" alt="Deno" width="25" height="25" />|Deno|![Deploy on Railway](https://railway.com/new/template/LsaSsU?utm_medium=integration&utm_source=button&utm_campaign=deno)|
|<img src="https://devicons.railway.com/i/bun.svg" alt="Bun" width="25" height="25" />|Bun|![Deploy on Railway](https://railway.com/new/template/gxxk5g?utm_medium=integration&utm_source=button&utm_campaign=bun)|
|<img src="https://devicons.railway.com/i/go.svg" alt="Gin" width="25" height="25" />|Gin|![Deploy on Railway](https://railway.com/new/template/dTvvSf?utm_medium=integration&utm_source=button&utm_campaign=gin)|
|<img src="https://devicons.railway.com/i/flask-dark.svg" alt="Flask" width="25" height="25" />|Flask|![Deploy on Railway](https://railway.com/new/template/zUcpux?utm_medium=integration&utm_source=button&utm_campaign=flask)|

## Kickback program

If your published template is deployed into other users' projects, you are eligible for kickbacks based on your support engagement. Learn more about the kickback program.

## Template verification

Templates are verified when the creator and maintainer of the technology becomes a partner and reviews the template.

If you are or have a relationship with the creator, please reach out to us by submitting the form on the partners page.

## Code Examples

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/new/template/ZweBXA?utm_medium=integration&utm_source=button&utm_campaign=generic)

<a
  href="https://railway.com/new/template/ZweBXA?utm_medium=integration&utm_source=button&utm_campaign=generic"
  ><img src="https://railway.com/button.svg" alt="Deploy on Railway"
/></a>


# Kickbacks
Source: https://docs.railway.com/templates/kickbacks

Earn revenue from your templates through Railway's kickback program.

Read more about the kickback program here.

## Eligibility requirements

To be eligible for template kickbacks, your template must meet the following requirements:

- **Marketplace**: Your template must be published to the template marketplace. Private and unpublished templates are not eligible.
- **Terms of Service**: Your project must abide by Railway's Fair Use Policy and Terms of Service. Templates that violate Railway's Terms of Service may be removed and kickback payments deemed ineligible.

## Kickback rates

- Templates receive a **15%** kickback of the usage costs incurred by users deploying your template.
- Support Bonus: Additional **10% (25% total)** when actively supporting users via your Template Queue

## How earnings are calculated

Kickbacks are calculated based on the proportional resource usage cost of your template services. 

For example, if a user pays $20 in platform fees, then incurs $200 of usage from your template, you are eligible for up to a $50 kickback (25% of $200 for an open source template with active support).

**Minimum Payout:** The minimum kickback payout is $0.01. Any kickback amount below this threshold will not be processed.

## Supporting your template users

When users have questions about your template, they'll appear in your Template Queue in Central Station. You'll get an email when new questions come in, plus occasional reminders if questions are waiting. 

Answering these questions earns you the additional 10% support bonus and helps users deploy your template successfully.

Manage notification preferences in your account settings under "Template Queue Emails".

<Image src="https://res.cloudinary.com/railway/image/upload/v1764639904/Template_Queue_Email_Notifications_qbfqg9.png" alt="Template Queue Emails" width={1800} height={1284} quality={100} />

## Open Source Partner Program

If you're the owner of a technology used in Railway templates, you can join the Open Source & Technology Partners program to unlock extra perks like commission on templates using your technology, featured placement, and opens source product-management features.

## Earnings and withdrawals

By default, your template kickbacks are automatically converted into Railway Credits. But we also offer cash withdrawals. Visit the /earnings tab inside your account settings for more details. There you can add your details and request a withdrawal.

<Banner variant="warning">Cash withdrawals are **not** supported in countries like **Brazil, China, and Russia**. A full list of supported countries is available on the earnings page.</Banner>

### Withdrawal FAQ

#### How do I start earning cash?

Simply flip the switch on the Earnings page marked Direct Deposit to Railway Credits. This will stop auto-depositing your earnings into the Railway credits system. You will then begin accruing cash in your Available Balance.

#### How do I request a withdrawal?

Follow the instructions inside the Earnings tab. We use Stripe Connect to handle withdrawals. After completing the onboarding process, you will be able to request a withdrawal.

#### Why is my country not supported?

Due to local regulations and compliance requirements, certain regions are not eligible for cash withdrawals. You can choose from the 130+ countries that are supported in the onboarding process.

#### Can I make manual withdrawals to credits too?

Yes! Choose to Credits in the dropdown and then make your withdrawal request.

#### I have earned a lot of kickbacks from a template, but this page says my available balance is $0. Why?

The current kickback method is to automatically apply your kickbacks as Railway credits. You can opt out of this if you wish to start accruing cash.

#### Can I still use the older, automatic-credits setting?

Yes. This behavior is enabled by default. You can opt out of it, and back in to it, at any time. Simply use the switch on the Earnings page marked Direct Deposit to Railway Credits.

#### What is the minimum and maximum withdrawal amount?

For now, withdrawals may be made in $100 - $10,000 increments.

#### What is the timeframe from withdrawal request to payout?

Withdrawals are usually processed instantly. Once processed, the funds will usually take up to 10 business days to reach your account. Depending on your region and bank, this may take longer.

#### What if there are no questions for my template?

If there are no questions, you will receive the full 25% kickback for your template.


# Private Docker images
Source: https://docs.railway.com/templates/private-docker-images

Create templates with private Docker images to distribute proprietary code through Railway and uniquely monetize.

This is useful for:
- Maintainers who want to distribute solely through Railway to maximize earnings
- Products that are premium versions of open source projects
- Proprietary add-ons or plugins

## Setting up private images

To add a private Docker image to your template:

1. In the template editor, add a service with a Docker image source
2. Enter your registry credentials in the service settings (username and password for Dockerhub, username and access token for Github registry)
3. Railway encrypts and stores the credentials securely

When users deploy your template, Railway authenticates with your registry to pull the image. Users see that the service uses hidden registry credentials, but cannot access the credentials themselves.

<Banner variant="warning">
To protect your credentials, SSH access is disabled and users cannot modify the Docker image source for services with hidden registry credentials.
</Banner>

## Combining with kickbacks

Private image templates are eligible for the same kickback rates as other templates. You earn commission when users deploy and run your private image templates.

For open source maintainers, make a hosted-only version of your tooling to capitalize on the commission you get from Railway templates.


# Metrics
Source: https://docs.railway.com/templates/metrics

Track deployments, earnings, and health metrics for your published templates.



## Overview stats

<Image
src="https://res.cloudinary.com/railway/image/upload/v1770748412/docs/template_product_metrics_orprmy.png"
alt="Template metrics"
layout="responsive"
width={1200} height={631} quality={100} />

The metrics dashboard shows key stats for your template:

- **Deployments**: Total number of times your template has been deployed
- **Earnings**: Total earnings from your template
- **Support Health**: Percentage of user questions you've answered in your Template Queue, and whether you are eligible for the support commission bonus

## Extended metrics

*This section is under construction. Template metrics within Railway today are shown in aggregate, but we are planning to expand this view. In the meantime, please use the Gauge template documented below.*

To see time series on template volume and earnings, use the Gauge Template Metrics built by our community. Launch it within your workspace by following the instructions on the deploy page.

See the executive summary of your template earnings over time.
<Image
src="https://res.cloudinary.com/railway/image/upload/v1770754260/docs/bi.tinybox.dev_d_mydb27f_executive-summary_orgId1fromnow-30dtonowtimezonebrowser_bg_d9z6os.png"
alt="Community template metrics: executive summary"
layout="responsive"
width={1200} height={631} quality={100} />

Understand per-template usage breakdowns.
<Image
src="https://res.cloudinary.com/railway/image/upload/v1770754260/docs/bi.tinybox.dev_d_mydb27f_executive-summary_orgId1fromnow-30dtonowtimezonebrowser_1_bg_uqujfd.png"
alt="Community template metrics: per template breakdown"
layout="responsive"
width={1200} height={631} quality={100} />


# Open source technology partners
Source: https://docs.railway.com/templates/partners

Grow your open source projects and products on Railway.

Apply at railway.com/partners.

<video src="https://res.cloudinary.com/railway/video/upload/v1771430834/docs/oss_partner_video_j7gyuw.mp4" controls autoplay loop muted playsinline />

## Earn commission

When users deploy your technology on Railway, you earn a percentage of the usage. The more your community grows on Railway, the more you earn.

- Base rate: 15% of usage from your verified templates
- Support bonus: +10% (25% total) when you answer user questions

See Kickbacks for details on earnings and withdrawals.

## Manage your product

### Community management

Your Template Queue in Central Station surfaces questions from users deploying your templates. While Central Station is our support platform, we are expanding it to be the platform for OSS maintainers to support their users. Answer questions to:

- Help users succeed with your technology
- Catch bugs and potential product improvements
- Build community around your project
- Earn the support bonus

### Growth metrics

Template metrics show deployments, earnings, and support health for your published templates.

## Monetize with private images

Want to offer a premium version alongside your open source project? Private Docker images let you create templates with proprietary code that users can deploy without accessing your source.

If you choose to make these private images available only on Railway, you are guaranteed to get commission for your work through Railway's template marketplace and kickback program.

## Ways to partner

Apply at railway.com/partners. Your project must be open source or open-core. Once accepted, you'll be part of a thread with our team to guide you through onboarding.

### Open source partnership

For open source maintainers who want to create and manage their own templates on Railway.

**Onboarding process:**

1. **Template verification**: Create a template (if you haven't already) following our best practices guide. Reply in your partner thread for us to review and verify it.

2. **Documentation**: Write a standalone guide in your documentation showing how to deploy your technology on Railway. Send us the page for any feedback.

3. **Social promotion**: Once your template is verified and the documentation page is live, we'll engage with any social promotion you do. Send us a link in your partner thread.

**What you get:**
- Verified template badge and featured placement
- Product management of your OSS tool with the template queue and metrics
- Monetization through regular template commission & private Docker images

### Technology partnership

For open source technologies that already have community-created templates on Railway. Earn commission from all templates using your technology, not just ones you create.

**Additional benefits:**
- Commission on *all* templates using your technology (even ones you didn't create)
- A dedicated page for your technology on Railway for SEO and distribution (example)
- Extended co-marketing with Railway

You're listed as a "maintainer" on community templates you earn commission from.

**Onboarding process:**

1. **Template selection**: Reply in your partner thread with links to all templates that primarily feature your technology.

2. **Template verification**: We'll verify a small selection of templates as recommended ways to deploy on Railway. Let us know which ones you think are the best fit.

3. **Documentation**: Write a standalone guide in your documentation showing how to deploy the template(s) on Railway. Send it over and we'll provide feedback.

4. **Partner profile**: We'll create a partner profile for you with a dedicated page showing all templates using your technology.

5. **Social promotion**: Once the above are complete, we'll engage with any social promotion or co-marketing you'd like to do.

If you have any other questions, feel free to email partners@railway.com.



# Languages & frameworks
Source: https://docs.railway.com/languages & frameworks

# Express
Source: https://docs.railway.com/guides/express


# Fastify
Source: https://docs.railway.com/guides/fastify


# Nest.js
Source: https://docs.railway.com/guides/nest


# Remix
Source: https://docs.railway.com/guides/remix


# Nuxt
Source: https://docs.railway.com/guides/nuxt


# Astro
Source: https://docs.railway.com/guides/astro


# SvelteKit
Source: https://docs.railway.com/guides/sveltekit


# React
Source: https://docs.railway.com/guides/react


# Vue
Source: https://docs.railway.com/guides/vue


# Angular
Source: https://docs.railway.com/guides/angular


# Solid
Source: https://docs.railway.com/guides/solid


# Sails
Source: https://docs.railway.com/guides/sails


# FastAPI
Source: https://docs.railway.com/guides/fastapi


# Flask
Source: https://docs.railway.com/guides/flask


# Django
Source: https://docs.railway.com/guides/django


# Laravel
Source: https://docs.railway.com/guides/laravel


# Symfony
Source: https://docs.railway.com/guides/symfony


# Rails
Source: https://docs.railway.com/guides/rails


# Gin
Source: https://docs.railway.com/guides/gin


# Beego
Source: https://docs.railway.com/guides/beego


# Axum
Source: https://docs.railway.com/guides/axum


# Rocket
Source: https://docs.railway.com/guides/rocket


# Spring Boot
Source: https://docs.railway.com/guides/spring-boot


# Play
Source: https://docs.railway.com/guides/play


# Phoenix
Source: https://docs.railway.com/guides/phoenix


# Phoenix + Distillery
Source: https://docs.railway.com/guides/phoenix-distillery


# Luminus
Source: https://docs.railway.com/guides/luminus



# CLI
Source: https://docs.railway.com/cli

# Global options
Source: https://docs.railway.com/cli/global-options

Flags available across multiple Railway CLI commands.



## Service

The --service option, shorthand -s, specifies which service to target. You can use either the service name or service ID.

## Environment

The --environment option, shorthand -e, specifies which environment to target. You can use either the environment name or environment ID.

## JSON output

The --json option outputs results in JSON format, useful for scripting and automation.

## Skip confirmation

The --yes option, shorthand -y, skips confirmation prompts. Use this in scripts or CI/CD pipelines where interactive input isn't possible.

## Help

The --help option, shorthand -h, displays help information for any command.

## Version

The --version option displays the current Railway CLI version.

## Code Examples

railway logs --service backend
railway up --service api
railway variable list -s my-service

railway logs --environment staging
railway up --environment production
railway variable list -e dev

railway status --json
railway variable list --json
railway logs --json

railway down --yes
railway redeploy -y
railway environment delete staging --yes

railway --help
railway up --help
railway logs -h

railway --version


# Deploying
Source: https://docs.railway.com/cli/deploying

Learn how to deploy your applications to Railway using the CLI.



## Quick deploy

The simplest way to deploy is with railway up:

This command scans, compresses, and uploads your app's files to Railway. You'll see real-time deployment logs in your terminal.

Railway will build your code using Railpack or your Dockerfile, then deploy it.

## Deployment modes

### Attached mode (default)

By default, railway up streams build and deployment logs to your terminal:

This is useful for watching the build process and catching errors immediately.

### Detached mode

Use -d or --detach to return immediately after uploading:

The deployment continues in the background. Check status in the dashboard or with railway logs.

### CI mode

Use -c or --ci to stream only build logs and exit when the build completes:

This is ideal for CI/CD pipelines where you want to see the build output but don't need to wait for deployment logs. Use --json to output logs in JSON format (also implies CI mode).

## Targeting services and environments

### Deploy to a specific service

If your project has multiple services, the CLI will prompt you to choose. You can also specify directly:

### Deploy to a specific environment

### Deploy to a specific project

Use -p or --project to deploy to a project without linking:

**Note:** When using --project, the --environment flag is required.

## CI/CD integration

### Using project tokens

For automated deployments, use a Project Token instead of interactive login. Project tokens are scoped to a specific environment and can only perform deployment-related actions.

Some actions you can perform with a project token:
- Deploying code - railway up
- Redeploying a deployment - railway redeploy
- Viewing build and deployment logs - railway logs

### GitHub actions

Railway makes deployment status available to GitHub, so you can trigger actions after deployments complete.

#### Post-deployment actions

Use the deployment_status event to run commands after Railway deploys your app:

See the GitHub Actions Post-Deploy guide for more details.

#### PR environments with GitHub actions

Create Railway environments automatically for pull requests:

**Note:** If you are using a workspace project, ensure the token is scoped to your account, not a specific workspace.

See the GitHub Actions PR Environment guide for the complete setup.

## Redeploying

Redeploy the current deployment without uploading new code:

This is useful for:
- Applying environment variable changes
- Restarting a crashed service
- Triggering a fresh build with the same code

## Deploying a specific path

You can specify a path to deploy:

By default, Railway uses your project root as the archive base. Use --path-as-root to use the specified path as the archive root instead:

When running railway up from a subdirectory without a path argument, Railway still deploys from the project root. To deploy only a specific directory permanently, configure a root directory in your service settings.

## Ignoring files

By default, Railway respects your .gitignore file. To include ignored files in your deployment:

## Verbose output

For debugging deployment issues:

## Related

- CLI Reference - Complete CLI command documentation
- GitHub Autodeploys - Automatic deployments from GitHub
- GitHub Actions Post-Deploy - Run actions after deployment
- GitHub Actions PR Environment - Create environments for PRs

## Code Examples

# Link to your project first (if not already linked)
railway link

# Deploy the current directory
railway up

railway up

railway up -d

railway up --ci

railway up --service my-api

railway up --environment staging

railway up --project <project-id> --environment production

RAILWAY_TOKEN=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX railway up

name: Post-Deployment Actions

on:
  deployment_status:
    states: [success]

jobs:
  post-deploy:
    runs-on: ubuntu-latest
    if: github.event.deployment_status.state == 'success'
    steps:
      - name: Run post-deploy actions
        if: github.event.deployment.environment == 'production'
        run: |
          echo "Production deployment succeeded"
          # Add your post-deploy commands here

name: Manage PR environments (Railway)

on:
  pull_request:
    types: [opened, closed]

env:
  RAILWAY_API_TOKEN: ${{ secrets.RAILWAY_API_TOKEN }}
  LINK_PROJECT_ID: "your-project-id"
  DUPLICATE_FROM_ID: "environment-to-duplicate"

jobs:
  pr_opened:
    if: github.event.action == 'opened'
    runs-on: ubuntu-latest
    container: ghcr.io/railwayapp/cli:latest
    steps:
      - name: Link to project
        run: railway link --project ${{ env.LINK_PROJECT_ID }} --environment ${{ env.DUPLICATE_FROM_ID }}
      - name: Create Railway Environment for PR
        run: railway environment new pr-${{ github.event.pull_request.number }} --copy ${{ env.DUPLICATE_FROM_ID }}

  pr_closed:
    if: github.event.action == 'closed'
    runs-on: ubuntu-latest
    container: ghcr.io/railwayapp/cli:latest
    steps:
      - name: Link to project
        run: railway link --project ${{ env.LINK_PROJECT_ID }} --environment ${{ env.DUPLICATE_FROM_ID }}
      - name: Delete Railway Environment for PR
        run: railway environment delete pr-${{ github.event.pull_request.number }} || true

railway redeploy

railway up ./backend

railway up ./backend --path-as-root

railway up --no-gitignore

railway up --verbose


# Telemetry
Source: https://docs.railway.com/cli/telemetry

What the Railway CLI collects and how to opt out.



## What is collected

| Field | Description |
|-------|-------------|
| Command name | The command that was run (e.g. up, deploy) |
| Subcommand name | The subcommand, if any (e.g. list in variable list) |
| Duration | How long the command took to execute, in milliseconds |
| Success | Whether the command completed successfully |
| Error message | A truncated error message if the command fails |
| OS | The operating system (e.g. linux, macos, windows) |
| Architecture | The CPU architecture (e.g. x86_64, aarch64) |
| CLI version | The version of the Railway CLI |
| CI | Whether the command was run in a CI environment |

No project source code, or environment variable values are collected.

## Opting out

Set either environment variable to 1 to disable telemetry:

DO_NOT_TRACK follows the Console Do Not Track convention. RAILWAY_NO_TELEMETRY is a Railway-specific alternative.

## Code Examples

export DO_NOT_TRACK=1
# or
export RAILWAY_NO_TELEMETRY=1


# add
Source: https://docs.railway.com/cli/add

Add a service to your project.



## Usage



## Options

| Flag | Description |
|------|-------------|
| -d, --database <TYPE> | Add a database (postgres, mysql, redis, mongo) |
| -s, --service [NAME] | Create an empty service (optionally with a name) |
| -r, --repo <REPO> | Create a service from a GitHub repo |
| -i, --image <IMAGE> | Create a service from a Docker image |
| -v, --variables <KEY=VALUE> | Environment variables to set on the service |
| --verbose | Enable verbose logging |
| --json | Output in JSON format |

## Examples

### Interactive mode

Prompts you to select what type of service to add.

### Add a database

Add multiple databases at once:

### Add from GitHub repo

### Add from Docker image

### Create an empty service

With a specific name:

### Add with environment variables

## Behavior

When you add a service, it's automatically linked to your current directory. For databases, the new service is automatically deployed.

## Related

- railway service
- railway link

## Code Examples

railway add [OPTIONS]

railway add

railway add --database postgres

railway add --database postgres --database redis

railway add --repo user/my-repo

railway add --image nginx:latest

railway add --service

railway add --service my-api

railway add --service api --variables "PORT=3000" --variables "NODE_ENV=production"


# bucket
Source: https://docs.railway.com/cli/bucket

Manage project buckets.



## Usage

### Global options

| Flag | Description |
|------|-------------|
| -e, --environment <ENV> | Environment name or ID |
| -b, --bucket <BUCKET> | Bucket name or ID (used by delete, info, credentials, rename) |

### Subcommands

| Subcommand | Aliases | Description |
|------------|---------|-------------|
| list | ls | List buckets |
| create | add, new | Create a new bucket |
| delete | remove, rm | Delete a bucket |
| info | | Show bucket details |
| credentials | | Show or reset S3-compatible credentials |
| rename | | Rename a bucket |

## List buckets

List all buckets deployed in the current environment.

| Flag | Description |
|------|-------------|
| --json | Output in JSON format |

Default output:

With --json:

## Create a bucket

Create a new bucket and deploy it to the target environment. An optional name can be passed as a positional argument; if omitted, the API assigns a default.

| Flag | Description |
|------|-------------|
| -r, --region <REGION> | Bucket region. Prompted interactively if omitted. |
| --json | Output in JSON format |

Available regions:

| Code | Location |
|------|----------|
| sjc | US West, California |
| iad | US East, Virginia |
| ams | EU West, Amsterdam |
| sin | Asia Pacific, Singapore |

Default output:

If the environment has unmerged staged changes, the operation is staged instead of committed directly. This applies to create, delete, and any other config-patching subcommand:

With --json:

## Delete a bucket

Delete a bucket from the target environment. Requires confirmation unless --yes is passed.

| Flag | Description |
|------|-------------|
| -y, --yes | Skip confirmation |
| --2fa-code <CODE> | 2FA code for verification |
| --json | Output in JSON format |

Default output:

If the environment has unmerged staged changes, the deletion is staged instead of committed directly:

With --json:

## Show bucket info

Display bucket instance details including storage size, object count, and region.

| Flag | Description |
|------|-------------|
| --json | Output in JSON format |

Default output:

With --json:

## Show or reset credentials

Display S3-compatible credentials for the selected bucket. The default output uses AWS_*=value lines suitable for eval or piping into .env files. Pass --reset to invalidate existing credentials and generate new ones.

| Flag | Description |
|------|-------------|
| --reset | Reset S3 credentials (invalidates existing credentials) |
| -y, --yes | Skip confirmation when resetting (requires --reset) |
| --2fa-code <CODE> | 2FA code for verification when resetting (requires --reset) |
| --json | Output in JSON format |

Default output:

When --reset is used without --json, only a confirmation message is printed:

To view the new credentials after resetting, run railway bucket credentials again or use --reset --json.

With --json (both with and without --reset):

## Rename a bucket

Rename a bucket. Prompts for the new name interactively, or accepts --name.

| Flag | Description |
|------|-------------|
| -n, --name <NAME> | New bucket name. Prompted interactively if omitted. |
| --json | Output in JSON format |

Default output:

With --json:

## Related

- Storage buckets

## Code Examples

railway bucket <COMMAND> [OPTIONS]

railway bucket -b my-bucket -e production info

railway bucket list

my-bucket
another-bucket

[
  {
    "id": "bucket-id",
    "name": "my-bucket"
  },
  {
    "id": "another-bucket-id",
    "name": "another-bucket"
  }
]

railway bucket create my-bucket --region sjc

Created bucket my-bucket (sjc)

Created bucket my-bucket (sjc) and staged it for production (use 'railway environment edit' to commit)

{
  "id": "bucket-id",
  "name": "my-bucket",
  "region": "sjc",
  "staged": false,
  "committed": true
}

railway bucket delete
railway bucket delete --yes

Deleted bucket my-bucket

Staged deletion of bucket my-bucket for production (use 'railway environment edit' to commit)

{
  "id": "bucket-id",
  "name": "my-bucket",
  "staged": false,
  "committed": true
}

railway bucket info

Name:          my-bucket
Bucket ID:     bucket-id
Environment:   production
Region:        sjc
Storage:       1.2 GB
Objects:       3,456

{
  "id": "bucket-id",
  "name": "my-bucket",
  "environmentId": "environment-id",
  "environment": "production",
  "region": "sjc",
  "storageBytes": 1200000000,
  "storage": "1.2 GB",
  "objects": 3456
}

railway bucket credentials
railway bucket credentials --reset --yes

AWS_ENDPOINT_URL=https://storage.railway.app
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_S3_BUCKET_NAME=my-bucket-abc123
AWS_DEFAULT_REGION=auto
AWS_S3_URL_STYLE=virtual

Credentials reset for my-bucket

{
  "endpoint": "https://storage.railway.app",
  "accessKeyId": "your-access-key",
  "secretAccessKey": "your-secret-key",
  "bucketName": "my-bucket-abc123",
  "region": "auto",
  "urlStyle": "virtual"
}

railway bucket rename
railway bucket rename --name new-name

Renamed my-bucket -> new-name

{
  "id": "bucket-id",
  "name": "new-name"
}


# completion
Source: https://docs.railway.com/cli/completion

Generate shell completion scripts.



## Usage



## Supported shells

- bash
- zsh
- fish
- powershell
- elvish

## Examples

### Bash

Or add to your ~/.bashrc:

### Zsh

Or add to your ~/.zshrc:

### Fish

### PowerShell

## Related

- railway upgrade

## Code Examples

railway completion <SHELL>

railway completion bash > /etc/bash_completion.d/railway

source <(railway completion bash)

railway completion zsh > "${fpath[1]}/_railway"

source <(railway completion zsh)

railway completion fish > ~/.config/fish/completions/railway.fish

railway completion powershell >> $PROFILE


# connect
Source: https://docs.railway.com/cli/connect

Connect to a database's shell.



## Usage



## Options

| Flag | Description |
|------|-------------|
| -e, --environment <ENV> | Environment to pull variables from (defaults to linked environment) |

## Supported databases

| Database | Client Required |
|----------|-----------------|
| PostgreSQL | psql |
| MySQL | mysql |
| Redis | redis-cli |
| MongoDB | mongosh |

## Examples

### Connect to database (interactive)

Prompts you to select a database service if multiple exist.

### Connect to specific database

### Connect to database in specific environment

## Requirements

- The database must have a TCP Proxy enabled (public URL)
- The appropriate database client must be installed on your machine

## How it works

1. Detects the database type from the service's image
2. Fetches connection variables (DATABASE_PUBLIC_URL, REDIS_PUBLIC_URL, etc.)
3. Launches the appropriate database client with the connection string

## Related

- railway ssh
- railway run

## Code Examples

railway connect [SERVICE_NAME] [OPTIONS]

railway connect

railway connect postgres

railway connect postgres --environment staging


# delete
Source: https://docs.railway.com/cli/delete

Delete a project.



## Usage



## Options

| Flag | Description |
|------|-------------|
| -p, --project <ID\|NAME> | Project to delete |
| -y, --yes | Skip confirmation dialog |
| --2fa-code <CODE> | 2FA code for verification (if 2FA is enabled) |
| --json | Output in JSON format |

## Examples

### Interactive deletion

Prompts you to select a project and confirm deletion.

### Delete specific project

### Skip confirmation

### With 2FA Code

## Warning

This action is **permanent** and cannot be undone. All services, deployments, and data within the project will be deleted.

## Related

- railway init
- railway list

## Code Examples

railway delete [OPTIONS]

railway delete

railway delete --project my-old-project

railway delete --project my-old-project --yes

railway delete --project my-project --yes --2fa-code 123456


# deploy
Source: https://docs.railway.com/cli/deploy

Provision a template into your project.

**Note:** This command deploys pre-built templates (like databases). To deploy your own code, use railway up instead.

## Usage



## Options

| Flag | Description |
|------|-------------|
| -t, --template <CODE> | The template code to deploy |
| -v, --variable <KEY=VALUE> | Environment variables for the template |

## Examples

### Deploy a template (interactive)

### Deploy PostgreSQL

### Deploy with variables

### Deploy multiple templates

### Service-specific variables

Prefix variables with the service name:

## Template codes

Common template codes:
- postgres - PostgreSQL database
- mysql - MySQL database
- redis - Redis database
- mongo - MongoDB database

Find more templates at railway.com/deploy.

## Related

- railway add
- Templates

## Code Examples

railway deploy [OPTIONS]

railway deploy

railway deploy --template postgres

railway deploy --template postgres --variable "POSTGRES_USER=admin"

railway deploy --template postgres --template redis

railway deploy --template my-app --variable "Backend.PORT=3000"


# deployment
Source: https://docs.railway.com/cli/deployment

Manage deployments.



## Usage



## Subcommands

| Subcommand | Aliases | Description |
|------------|---------|-------------|
| list | ls | List deployments with IDs, statuses, and timestamps |
| up | | Upload and deploy (same as railway up) |
| redeploy | | Redeploy latest deployment (same as railway redeploy) |

## Examples

### List deployments

Output:


### List more deployments

### List deployments for specific service

### List deployments in JSON format

Useful for scripting:

### Use deployment ID with logs

## Options for `list`

| Flag | Description |
|------|-------------|
| -s, --service <SERVICE> | Service to list deployments for (defaults to linked service) |
| -e, --environment <ENV> | Environment to list deployments from (defaults to linked environment) |
| --limit <N> | Maximum number of deployments to show (default: 20, max: 1000) |
| --json | Output in JSON format |

## Deployment statuses

| Status | Description |
|--------|-------------|
| SUCCESS | Deployment completed successfully |
| FAILED | Deployment failed |
| CRASHED | Deployment crashed after starting |
| BUILDING | Deployment is being built |
| DEPLOYING | Deployment is being deployed |
| INITIALIZING | Deployment is initializing |
| WAITING | Deployment is waiting |
| QUEUED | Deployment is queued |
| REMOVED | Deployment was removed |
| REMOVING | Deployment is being removed |

## Related

- railway up
- railway redeploy
- railway logs

## Code Examples

railway deployment <COMMAND> [OPTIONS]

railway deployment list

Recent Deployments
  7422c95b-c604-46bc-9de4-b7a43e1fd53d | SUCCESS | 2024-01-15 10:30:00 PST
  a1b2c3d4-e5f6-7890-abcd-ef1234567890 | FAILED | 2024-01-15 09:15:00 PST
  ...

railway deployment list --limit 50

railway deployment list --service backend

railway deployment list --json

# Get the latest deployment ID
railway deployment list --json --limit 1 | jq -r '.[0].id'

# Get deployment ID from list
railway deployment list

# View logs for specific deployment
railway logs 7422c95b-c604-46bc-9de4-b7a43e1fd53d


# dev
Source: https://docs.railway.com/cli/dev

Run Railway services locally.

**Note:** This is an experimental feature. The API may change without notice.

## Usage



## Aliases

- railway develop

## Subcommands

| Subcommand | Description |
|------------|-------------|
| up | Start services (default) |
| down | Stop services |
| clean | Stop services and remove volumes/data |
| configure | Configure local code services |

## Examples

### Start local development

Starts image-based services (databases, etc.) via Docker Compose and prompts you to configure code-based services.

### Start with verbose output

### Stop services

### Clean up (remove data)

### Configure Code services

Interactively configure how your code services run locally (command, directory, port).

## Options for `up`

| Flag | Description |
|------|-------------|
| -e, --environment <ENV> | Environment to use |
| -o, --output <PATH> | Output path for docker-compose.yml |
| --dry-run | Generate docker-compose.yml without starting |
| --no-https | Disable HTTPS and pretty URLs |
| -v, --verbose | Show verbose domain replacement info |
| --no-tui | Disable TUI, stream logs to stdout |

## Options for `configure`

| Flag | Description |
|------|-------------|
| --service <SERVICE> | Specific service to configure (by name) |
| --remove [SERVICE] | Remove configuration for a service (optionally specify service name) |

### Configure examples

Configure a specific service:

Remove configuration for all services:

Remove configuration for a specific service:

## Requirements

- Docker with Docker Compose
- mkcert (optional, for HTTPS support)

## How it works

1. Fetches environment configuration from Railway
2. Generates a docker-compose.yml for image-based services (databases, etc.)
3. Starts containers with proper environment variables
4. Optionally runs code services locally with injected environment variables
5. Sets up a Caddy reverse proxy for HTTPS (if mkcert is available)

## Related

- railway run
- railway shell

## Code Examples

railway dev [COMMAND] [OPTIONS]

railway dev

railway dev --verbose

railway dev down

railway dev clean

railway dev configure

railway dev configure --service backend

railway dev configure --remove

railway dev configure --remove backend


# docs
Source: https://docs.railway.com/cli/docs

Open Railway Documentation in the browser.



## Usage



## Examples

Opens docs.railway.com in your default browser.

## Related

- railway open

## Code Examples

railway docs

railway docs


# domain
Source: https://docs.railway.com/cli/domain

Add a domain to a service.



## Usage



## Options

| Flag | Description |
|------|-------------|
| -p, --port <PORT> | The port to connect to the domain |
| -s, --service <SERVICE> | The service to add the domain to |
| --json | Output in JSON format |

## Examples

### Generate a Railway domain

Creates a free *.up.railway.app domain for your service.

### Add a custom domain

Returns the required DNS records to configure.

### Add domain with specific port

### Add domain to specific service

## Custom domain setup

When adding a custom domain, the CLI displays the required DNS records:

DNS changes can take up to 72 hours to propagate worldwide.

## Limits

- One Railway-provided domain per service
- Multiple custom domains can be added per service

## Related

- Domains
- railway service

## Code Examples

railway domain [DOMAIN] [OPTIONS]

railway domain

railway domain example.com

railway domain example.com --port 8080

railway domain example.com --service api

To finish setting up your custom domain, add the following DNS records to example.com:

    Type     Name    Value
    CNAME    @       your-service.up.railway.app


# down
Source: https://docs.railway.com/cli/down

Remove the most recent deployment.



## Usage



## Options

| Flag | Description |
|------|-------------|
| -s, --service <SERVICE> | Service to remove deployment from (defaults to linked service) |
| -e, --environment <ENV> | Environment to remove deployment from (defaults to linked environment) |
| -y, --yes | Skip confirmation dialog |

## Examples

### Remove latest deployment

### Remove from specific service

### Skip confirmation

## Behavior

This command removes only the latest successful deployment. The service itself is not deleted, and you can deploy again with railway up.

## Related

- railway up
- railway redeploy

## Code Examples

railway down [OPTIONS]

railway down

railway down --service backend

railway down --yes


# environment
Source: https://docs.railway.com/cli/environment

Manage environments.



## Usage



## Aliases

- railway env

## Subcommands

| Subcommand | Description |
|------------|-------------|
| link | Link an environment to the current project |
| new | Create a new environment |
| delete | Delete an environment |
| edit | Edit an environment's configuration |
| config | Show environment configuration |

## Examples

### Link an environment (interactive)

### Link a specific environment

### Create a new environment

### Duplicate an environment

Or using the alias:

### Delete an environment

### Edit environment configuration

### Show environment configuration

## Options for `new`

| Flag | Description |
|------|-------------|
| -d, --duplicate <ENV> | Environment to duplicate (alias: --copy) |
| --json | Output in JSON format |

## Options for `delete`

| Flag | Description |
|------|-------------|
| -y, --yes | Skip confirmation dialog |
| --2fa-code <CODE> | 2FA code for verification |
| --json | Output in JSON format |

## Options for `edit`

| Flag | Description |
|------|-------------|
| -e, --environment <ENV> | Environment to edit |
| -s, --service-config <SERVICE> <PATH> <VALUE> | Configure a service using dot-path notation |
| -m, --message <MSG> | Commit message for the changes |
| --stage | Stage changes without committing |
| --json | Output in JSON format |

### Dot-path notation for --service-config

The --service-config flag uses dot-path notation to specify nested configuration values:

The format is: --service-config <SERVICE_NAME> <DOT.PATH.TO.PROPERTY> <VALUE>

## Options for `config`

| Flag | Description |
|------|-------------|
| -e, --environment <ENV> | Environment to show configuration for (defaults to linked environment) |
| --json | Output in JSON format |

### Config examples

Show configuration for the current environment:

Show configuration for a specific environment:

Output as JSON:

## Related

- railway link
- Environments

## Code Examples

railway environment [ENVIRONMENT] [COMMAND]

railway environment

railway environment staging

railway environment new staging

railway environment new staging --duplicate production

railway environment new staging --copy production

railway environment delete staging

railway environment edit --service-config backend variables.API_KEY.value "secret"

railway environment config

# Set a variable value
railway environment edit --service-config backend variables.API_KEY.value "secret"

# Set a service configuration
railway environment edit --service-config api buildCommand "npm run build"

railway environment config

railway environment config --environment staging

railway environment config --json


# functions
Source: https://docs.railway.com/cli/functions

Manage project functions.



## Usage



## Aliases

- railway function
- railway func
- railway fn
- railway funcs
- railway fns

## Subcommands

| Subcommand | Aliases | Description |
|------------|---------|-------------|
| list | ls | List functions |
| new | create | Add a new function |
| delete | remove, rm | Delete a function |
| push | up | Push changes to a function |
| pull | | Pull changes from a linked function |
| link | | Link a function manually |

## Examples

### List functions

### Create a new function

### Create an HTTP function

### Create a cron function

### Push changes

### Push with watch mode

### Pull remote changes

### Delete a function

### Link a function

## Options for `new`

| Flag | Description |
|------|-------------|
| -p, --path <PATH> | Path to the function file |
| -n, --name <NAME> | Name of the function |
| -c, --cron <SCHEDULE> | Cron schedule for the function |
| --http | Generate a domain for HTTP access |
| -s, --serverless | Enable serverless mode (sleeping) |
| -w, --watch | Watch for changes and deploy on save |

## Options for `push`

| Flag | Description |
|------|-------------|
| -p, --path <PATH> | Path to the function |
| -w, --watch | Watch for changes and deploy on save |

## Options for `delete`

| Flag | Description |
|------|-------------|
| -f, --function <FUNCTION> | ID or name of the function to delete |
| -y, --yes | Skip confirmation dialog |

## Common options

| Flag | Description |
|------|-------------|
| -e, --environment <ENV> | Environment ID or name |

## Related

- Functions

## Code Examples

railway functions <COMMAND> [OPTIONS]

railway functions list

railway functions new --path ./my-function.ts --name my-function

railway functions new --path ./api.ts --name api --http

railway functions new --path ./job.ts --name cleanup --cron "0 * * * *"

railway functions push

railway functions push --watch

railway functions pull

railway functions delete --function my-function

railway functions link --function my-function --path ./local-function.ts


# init
Source: https://docs.railway.com/cli/init

Create a new project.



## Usage



## Aliases

- railway new

## Options

| Flag | Description |
|------|-------------|
| -n, --name <NAME> | Project name (randomly generated if not provided) |
| -w, --workspace <ID\|NAME> | Workspace to create the project in |
| --json | Output in JSON format |

## Examples

### Interactive project creation

Prompts you to select a workspace and enter a project name.

### Create with specific name

### Create in specific workspace

### Non-interactive (CI/CD)

## Output

After creation, the project is automatically linked to your current directory. You can start deploying with railway up.

## Related

- railway link
- railway up
- railway project

## Code Examples

railway init [OPTIONS]

railway init

railway init --name my-api

railway init --name my-api --workspace "My Team"

railway init --name my-api --workspace my-team-id --json


# link
Source: https://docs.railway.com/cli/link

Associate an existing project with the current directory.



## Usage



## Options

| Flag | Description |
|------|-------------|
| -p, --project <ID\|NAME> | Project to link to |
| -e, --environment <ID\|NAME> | Environment to link to |
| -s, --service <ID\|NAME> | Service to link to |
| -w, --workspace <ID\|NAME> | Workspace to link to |
| -t, --team <ID\|NAME> | Team to link to (deprecated, use --workspace) |
| --json | Output in JSON format |

## Examples

### Interactive linking

Prompts you to select a workspace, project, environment, and optionally a service.

### Link to specific project

### Link to specific environment

### Link to specific service

### Non-interactive (CI/CD)

## How it works

Railway stores the link configuration in a .railway directory in your project root. This file is typically added to .gitignore.

The link includes:
- Project ID
- Environment ID
- Service ID (optional)

## Related

- railway unlink
- railway init
- railway status

## Code Examples

railway link [OPTIONS]

railway link

railway link --project my-api

railway link --project my-api --environment staging

railway link --project my-api --service backend

railway link --project abc123 --environment def456 --json


# list
Source: https://docs.railway.com/cli/list

List all projects in your Railway account.



## Usage



## Options

| Flag | Description |
|------|-------------|
| --json | Output in JSON format |

## Examples

### List all projects

Output:


The currently linked project is highlighted in purple.

### JSON output

Returns an array of all projects with their workspace information.

## Related

- railway link
- railway init
- railway project

## Code Examples

railway list [OPTIONS]

railway list

My Team
  my-api
  frontend-app

Personal
  side-project

railway list --json


# login
Source: https://docs.railway.com/cli/login

Login to your Railway account.



## Usage



## Options

| Flag | Description |
|------|-------------|
| -b, --browserless | Login without opening a browser (uses pairing code) |

## Examples

### Browser login (default)

Opens your default browser to authenticate:

### Browserless login

Use this in environments without a browser (e.g., SSH sessions):

This displays a pairing code and URL. Visit the URL and enter the code to authenticate.

## Environment variables

If RAILWAY_TOKEN or RAILWAY_API_TOKEN is set, the CLI will use that token instead of prompting for login. See Tokens for more information.

## Related

- railway logout
- railway whoami
- Global Options

## Code Examples

railway login [OPTIONS]

railway login

railway login --browserless


# logout
Source: https://docs.railway.com/cli/logout

Logout of your Railway account.



## Usage



## Examples

This clears your stored authentication token. You'll need to run railway login again to use authenticated commands.

## Related

- railway login
- railway whoami

## Code Examples

railway logout

railway logout


# logs
Source: https://docs.railway.com/cli/logs

View build or deploy logs from a Railway deployment.



## Usage



## Options

| Flag | Description |
|------|-------------|
| -s, --service <SERVICE> | Service to view logs from (defaults to linked service) |
| -e, --environment <ENV> | Environment to view logs from (defaults to linked environment) |
| -d, --deployment | Show deployment logs |
| -b, --build | Show build logs |
| -n, --lines <N> | Number of log lines to fetch (disables streaming) |
| -f, --filter <QUERY> | Filter logs using Railway's query syntax |
| --latest | Show logs from latest deployment (even if failed/building) |
| -S, --since <TIME> | Show logs since a specific time (disables streaming) |
| -U, --until <TIME> | Show logs until a specific time (disables streaming) |
| --json | Output logs in JSON format |

## Examples

### Stream live logs

### View build logs

### View last 100 lines

### View logs from last hour

### View logs from time range

### View logs since specific time

### Filter error logs

### Filter warning logs with text

### Logs from specific service

### Logs from specific deployment

### JSON output

## Time formats

The --since and --until flags accept:

- **Relative times**: 30s, 5m, 2h, 1d, 1w
- **ISO 8601 timestamps**: 2024-01-15T10:30:00Z

## Filter syntax

Railway uses a query syntax for filtering logs:

- **Text search**: "error message" or user signup
- **Attribute filters**: @level:error, @level:warn
- **Operators**: AND, OR, - (not)

See Logs for full syntax documentation.

## Behavior

- **Stream mode** (default): Connects via WebSocket and streams logs in real-time
- **Fetch mode**: Retrieves historical logs when using --lines, --since, or --until
- If the latest deployment failed, build logs are shown by default

## Related

- railway ssh
- Logs

## Code Examples

railway logs [DEPLOYMENT_ID] [OPTIONS]

railway logs

railway logs --build

railway logs --lines 100

railway logs --since 1h

railway logs --since 30m --until 10m

railway logs --since 2024-01-15T10:00:00Z

railway logs --lines 10 --filter "@level:error"

railway logs --lines 10 --filter "@level:warn AND rate limit"

railway logs --service backend --environment production

railway logs 7422c95b-c604-46bc-9de4-b7a43e1fd53d --build

railway logs --json


# open
Source: https://docs.railway.com/cli/open

Open your project dashboard in the browser.



## Usage



## Options

| Flag | Description |
|------|-------------|
| -p, --print | Print the URL instead of opening it |

## Examples

### Open dashboard

Opens the project dashboard in your default browser.

### Print URL only

Outputs the dashboard URL without opening it. Useful for copying or scripting.

## Related

- railway status
- railway link

## Code Examples

railway open [OPTIONS]

railway open

railway open --print


# project
Source: https://docs.railway.com/cli/project

Manage projects.



## Usage



## Subcommands

| Subcommand | Aliases | Description |
|------------|---------|-------------|
| list | ls | List all projects in your account |
| link | | Link a project to the current directory |
| delete | rm, remove | Delete a project |

## Examples

### List all projects

### Link a project

### Delete a project

## Related

- railway init
- railway link
- railway list
- railway delete

## Code Examples

railway project <COMMAND>

railway project list

railway project link

railway project delete --project my-old-project


# redeploy
Source: https://docs.railway.com/cli/redeploy

Redeploy the latest deployment of a service.



## Usage



## Options

| Flag | Description |
|------|-------------|
| -s, --service <SERVICE> | Service to redeploy (defaults to linked service) |
| -y, --yes | Skip confirmation dialog |
| --json | Output in JSON format |

## Examples

### Redeploy current service

### Redeploy specific service

### Skip confirmation

## Use cases

Redeploying is useful for:
- Applying environment variable changes
- Restarting a service that crashed
- Triggering a fresh deployment with the same code

## Related

- railway up
- railway restart
- railway logs

## Code Examples

railway redeploy [OPTIONS]

railway redeploy

railway redeploy --service backend

railway redeploy --yes


# restart
Source: https://docs.railway.com/cli/restart

Restart the latest deployment of a service (without rebuilding).



## Usage



## Options

| Flag | Description |
|------|-------------|
| -s, --service <SERVICE> | Service to restart (defaults to linked service) |
| -y, --yes | Skip confirmation dialog |
| --json | Output in JSON format |

## Examples

### Restart current service

### Restart specific service

### Skip confirmation

## Behavior

This command restarts the service without rebuilding it. The existing deployment image is reused. The command waits for the deployment to become healthy before completing.

## Difference from redeploy

- **restart**: Restarts the existing deployment (no build)
- **redeploy**: Creates a new deployment from the same source (triggers a build)

## Related

- railway redeploy
- railway logs

## Code Examples

railway restart [OPTIONS]

railway restart

railway restart --service backend

railway restart --yes


# run
Source: https://docs.railway.com/cli/run

Run a local command using variables from the active environment.



## Usage



## Aliases

- railway local

## Options

| Flag | Description |
|------|-------------|
| -s, --service <SERVICE> | Service to pull variables from (defaults to linked service) |
| -e, --environment <ENV> | Environment to pull variables from (defaults to linked environment) |
| -p, --project <ID> | Project ID to use (defaults to linked project) |
| --no-local | Skip local develop overrides |
| -v, --verbose | Show verbose domain replacement info |

## Examples

### Run a Node.js app

### Run a Python script

### Run with specific service variables

### Run database migrations

### Access a repl

## How it works

1. Fetches environment variables from the specified Railway service
2. Injects them into the command's environment
3. Executes the command

This is useful for:
- Running your app locally with production/staging variables
- Running database migrations
- Accessing REPLs with the correct environment

## Exit codes

The command exits with the same code as the executed command.

## Related

- railway shell
- railway dev

## Code Examples

railway run [OPTIONS] <COMMAND> [ARGS...]

railway run npm start

railway run python main.py

railway run --service backend npm start

railway run npx prisma migrate deploy

railway run rails console
railway run python


# scale
Source: https://docs.railway.com/cli/scale

Scale a service across regions.



## Usage



## Options

| Flag | Description |
|------|-------------|
| -s, --service <SERVICE> | Service to scale (defaults to linked service) |
| -e, --environment <ENV> | Environment the service is in (defaults to linked environment) |
| --json | Output in JSON format |
| --<REGION>=<N> | Set the number of instances for a specific region |

## Dynamic region flags

The available region flags are fetched dynamically from Railway. Common regions include:

- --us-west1
- --us-east4
- --europe-west4
- --asia-southeast1

## Examples

### Interactive mode

Prompts you to select regions and instance counts.

### Scale to specific regions

### Scale specific service

## Behavior

After updating the region configuration, the service is automatically redeployed to apply the changes.

## Related

- railway redeploy
- Scaling

## Code Examples

railway scale [OPTIONS] [--<REGION>=<INSTANCES>...]

railway scale

railway scale --us-west1=2 --us-east4=1

railway scale --service backend --us-west1=3


# service
Source: https://docs.railway.com/cli/service

Manage services.



## Usage



## Subcommands

| Subcommand | Description |
|------------|-------------|
| link | Link a service to the current project |
| status | Show deployment status for services |
| logs | View logs from a service |
| redeploy | Redeploy the latest deployment |
| restart | Restart the latest deployment |
| scale | Scale a service across regions |

## Examples

### Link a service (interactive)

Prompts you to select a service to link.

### Link a specific service

### Show service status

### Show all services status

### View service logs

### Redeploy service

### Restart service

### Scale service

## Options for `status`

| Flag | Description |
|------|-------------|
| -a, --all | Show status for all services in the environment |
| --json | Output in JSON format |

## Options for `logs`

| Flag | Description |
|------|-------------|
| -d, --deployment | Show deployment logs |
| -b, --build | Show build logs |
| -n, --lines <N> | Number of log lines to fetch (disables streaming) |
| -f, --filter <QUERY> | Filter logs using Railway's query syntax |
| --latest | Show logs from latest deployment (even if failed/building) |
| -S, --since <TIME> | Show logs since a specific time |
| -U, --until <TIME> | Show logs until a specific time |
| --json | Output logs in JSON format |

See railway logs for detailed usage and examples.

## Options for `redeploy`

| Flag | Description |
|------|-------------|
| -y, --yes | Skip confirmation dialog |
| --json | Output in JSON format |

## Options for `restart`

| Flag | Description |
|------|-------------|
| -y, --yes | Skip confirmation dialog |
| --json | Output in JSON format |

## Options for `scale`

| Flag | Description |
|------|-------------|
| --<REGION>=<N> | Set the number of instances for a specific region |
| --json | Output in JSON format |

See railway scale for available regions and detailed usage.

## Related

- railway add
- railway link
- railway logs

## Code Examples

railway service [SERVICE] [COMMAND]

railway service

railway service backend

railway service status

railway service status --all

railway service logs

railway service redeploy

railway service restart

railway service scale --us-west1=2


# shell
Source: https://docs.railway.com/cli/shell

Open a local subshell with Railway variables available.



## Usage



## Options

| Flag | Description |
|------|-------------|
| -s, --service <SERVICE> | Service to pull variables from (defaults to linked service) |
| --silent | Open shell without banner |

## Examples

### Open shell with variables

Output:


### Shell for specific service

### Silent mode

## How it works

1. Fetches environment variables from the specified Railway service
2. Opens a new shell with those variables in the environment
3. Sets IN_RAILWAY_SHELL=true to indicate you're in a Railway shell

Type exit to leave the shell and return to your normal environment.

## Shell detection

On Windows, the CLI detects your current shell (PowerShell, cmd, pwsh) and opens the same type. On Unix systems, it uses the $SHELL environment variable.

## Difference from `railway run`

- **shell**: Opens an interactive shell session
- **run**: Executes a single command and exits

## Related

- railway run
- railway dev

## Code Examples

railway shell [OPTIONS]

railway shell

Entering subshell with Railway variables available. Type 'exit' to exit.

railway shell --service backend

railway shell --silent


# ssh
Source: https://docs.railway.com/cli/ssh

Connect to a service via SSH.



## Usage



## Options

| Flag | Description |
|------|-------------|
| -p, --project <ID> | Project to connect to (defaults to linked project) |
| -s, --service <SERVICE> | Service to connect to (defaults to linked service) |
| -e, --environment <ENV> | Environment to connect to (defaults to linked environment) |
| -d, --deployment-instance <ID> | Specific deployment instance ID to connect to |
| --session [NAME] | Use a tmux session (installs tmux if needed) |

## Examples

### Interactive shell

Opens a bash shell in the service container.

### Run a single command

### SSH with tmux session

Creates a persistent tmux session that reconnects automatically if disconnected.

### SSH to specific service

## Use cases

- Debugging production issues
- Running database migrations
- Accessing language REPLs (Rails console, Django shell, etc.)
- Inspecting log files
- Troubleshooting network issues

## How it works

Railway SSH uses a custom WebSocket-based protocol (not standard SSH). This means:

- No SSH daemon required in your container
- Secure communication through Railway's authentication
- Works with any container that has a shell available

## Limitations

- No SCP/SFTP file transfer
- No SSH tunneling or port forwarding
- No IDE integration (VS Code Remote-SSH)

## Related

- railway connect
- railway logs

## Code Examples

railway ssh [OPTIONS] [COMMAND...]

railway ssh

railway ssh -- ls -la

railway ssh --session

railway ssh --service backend


# starship
Source: https://docs.railway.com/cli/starship

Output metadata for Starship prompt integration.



## Usage

This command is primarily used for Starship prompt integration to display Railway project information in your terminal prompt.

## Output

Returns JSON containing the linked project information:

## Related

- railway status

## Code Examples

railway starship

{
  "project": "project-id",
  "name": "my-project",
  "environment": "environment-id",
  "environmentName": "production"
}


# status
Source: https://docs.railway.com/cli/status

Show information about the current project.



## Usage



## Options

| Flag | Description |
|------|-------------|
| --json | Output in JSON format |

## Examples

### Show current status

Output:


### JSON output

Returns detailed project information including all services and environments.

## Related

- railway link
- railway open

## Code Examples

railway status [OPTIONS]

railway status

Project: my-api
Environment: production
Service: backend

railway status --json


# unlink
Source: https://docs.railway.com/cli/unlink

Disassociate project from current directory.



## Usage



## Options

| Flag | Description |
|------|-------------|
| -s, --service | Unlink only the service (keep project link) |
| -y, --yes | Skip confirmation prompt |
| --json | Output in JSON format |

## Examples

### Unlink project

Removes the entire project link from the current directory.

### Unlink service only

Keeps the project and environment link but removes the service association.

### Skip confirmation

Useful for scripts and automation.

## Related

- railway link
- railway status

## Code Examples

railway unlink [OPTIONS]

railway unlink

railway unlink --service

railway unlink --yes


# up
Source: https://docs.railway.com/cli/up

Upload and deploy project from the current directory.

**Note:** This command uploads and deploys your local code. To deploy pre-built templates (like databases), use railway deploy instead.

## Usage



## Options

| Flag | Description |
|------|-------------|
| -d, --detach | Don't attach to the log stream |
| -c, --ci | Stream build logs only, then exit (CI mode) |
| -s, --service <SERVICE> | Service to deploy to (defaults to linked service) |
| -e, --environment <ENV> | Environment to deploy to (defaults to linked environment) |
| -p, --project <ID> | Project ID to deploy to (defaults to linked project) |
| --no-gitignore | Don't ignore paths from .gitignore |
| --path-as-root | Use the path argument as the archive root |
| --verbose | Verbose output |
| --json | Output logs in JSON format (implies CI mode) |

## Examples

### Basic deploy

Compresses and uploads the current directory, then streams build and deployment logs.

### Deploy in detached mode

Uploads the project and returns immediately without streaming logs.

### Deploy to specific service

### Deploy to specific environment

### CI/CD mode

Streams build logs only and exits when the build completes. Useful for CI/CD pipelines.

### Deploy a subdirectory

## File handling

By default, railway up:
- Respects your .gitignore file
- Respects .railwayignore file (Railway-specific ignore patterns)
- Ignores .git and node_modules directories

Use --no-gitignore to include files that would normally be ignored.

## Exit codes

- 0 - Deployment succeeded
- 1 - Deployment failed or crashed

## Related

- railway redeploy
- railway logs
- Deploying with the CLI

## Code Examples

railway up [PATH] [OPTIONS]

railway up

railway up --detach

railway up --service backend

railway up --environment staging

railway up --ci

railway up ./backend


# upgrade
Source: https://docs.railway.com/cli/upgrade

Upgrade the Railway CLI to the latest version.



## Usage



## Options

| Flag | Description |
|------|-------------|
| --check | Show install method and upgrade command without upgrading |

## Examples

### Upgrade CLI

Automatically detects your install method and runs the appropriate upgrade command.

### Check install method

Output:


## Supported install methods

| Method | Upgrade Command |
|--------|----------------|
| Homebrew | brew upgrade railway |
| npm | npm update -g @railway/cli |
| Bun | bun update -g @railway/cli |
| Cargo | cargo install railwayapp |
| Scoop | scoop update railway |
| Shell | bash <(curl -fsSL cli.new) |

## Manual upgrade

If automatic detection fails, you can manually run the upgrade command for your install method.

## Related

- CLI Installation

## Code Examples

railway upgrade [OPTIONS]

railway upgrade

railway upgrade --check

Install method: Homebrew
Binary path: /opt/homebrew/bin/railway
Upgrade command: brew upgrade railway


# variable
Source: https://docs.railway.com/cli/variable

Manage environment variables.



## Usage



## Aliases

- railway variables
- railway vars
- railway var

## Subcommands

| Subcommand | Aliases | Description |
|------------|---------|-------------|
| list | ls | List variables for a service |
| set | | Set a variable |
| delete | rm, remove | Delete a variable |

## Examples

### List variables

### List in key-value format

Output:


### Set a variable

### Set multiple variables

### Set variable from stdin

### Delete a variable

## Options for `list`

| Flag | Description |
|------|-------------|
| -s, --service <SERVICE> | Service to list variables for |
| -e, --environment <ENV> | Environment to list variables from |
| -k, --kv | Show variables in KEY=VALUE format |
| --json | Output in JSON format |

## Options for `set`

| Flag | Description |
|------|-------------|
| -s, --service <SERVICE> | Service to set the variable for |
| -e, --environment <ENV> | Environment to set the variable in |
| --stdin | Read value from stdin (use with single KEY) |
| --skip-deploys | Skip triggering deploys |
| --json | Output in JSON format |

## Options for `delete`

| Flag | Description |
|------|-------------|
| -s, --service <SERVICE> | Service to delete the variable from |
| -e, --environment <ENV> | Environment to delete the variable from |
| --json | Output in JSON format |

## Legacy flags

The following flags are deprecated but still supported:

## Related

- Variables
- railway run

## Code Examples

railway variable [COMMAND] [OPTIONS]

railway variable list

railway variable list --kv

DATABASE_URL=postgres://...
API_KEY=secret123

railway variable set API_KEY=secret123

railway variable set API_KEY=secret123 DEBUG=true

echo "my-secret-value" | railway variable set SECRET_KEY --stdin

railway variable delete API_KEY

# Deprecated: use 'Railway variable set KEY=VALUE' instead
railway variable --set KEY=VALUE

# Deprecated: use 'Railway variable set key --stdin' instead
railway variable --set-from-stdin KEY


# volume
Source: https://docs.railway.com/cli/volume

Manage project volumes.



## Usage



## Subcommands

| Subcommand | Aliases | Description |
|------------|---------|-------------|
| list | ls | List volumes |
| add | create | Add a new volume |
| delete | remove, rm | Delete a volume |
| update | edit | Update a volume |
| detach | | Detach a volume from a service |
| attach | | Attach a volume to a service |

## Examples

### List volumes

### Add a volume

### Delete a volume

### Update volume mount path

### Rename a volume

### Detach volume from service

### Attach volume to service

## Common options

| Flag | Description |
|------|-------------|
| -s, --service <SERVICE> | Service ID |
| -e, --environment <ENV> | Environment ID |
| --json | Output in JSON format |

## Options for `add`

| Flag | Description |
|------|-------------|
| -m, --mount-path <PATH> | Mount path for the volume (must start with /) |

## Options for `delete`

| Flag | Description |
|------|-------------|
| -v, --volume <VOLUME> | Volume ID or name |
| -y, --yes | Skip confirmation |
| --2fa-code <CODE> | 2FA code for verification |

## Options for `update`

| Flag | Description |
|------|-------------|
| -v, --volume <VOLUME> | Volume ID or name |
| -m, --mount-path <PATH> | New mount path |
| -n, --name <NAME> | New name for the volume |

## Options for `detach`

| Flag | Description |
|------|-------------|
| -v, --volume <VOLUME> | Volume ID or name to detach |
| -y, --yes | Skip confirmation |
| --json | Output in JSON format |

## Options for `attach`

| Flag | Description |
|------|-------------|
| -v, --volume <VOLUME> | Volume ID or name to attach |
| -y, --yes | Skip confirmation |
| --json | Output in JSON format |

## Related

- Volumes

## Code Examples

railway volume <COMMAND> [OPTIONS]

railway volume list

railway volume add --mount-path /data

railway volume delete --volume my-volume

railway volume update --volume my-volume --mount-path /new/path

railway volume update --volume my-volume --name new-name

railway volume detach --volume my-volume

railway volume attach --volume my-volume --service backend


# whoami
Source: https://docs.railway.com/cli/whoami

Get the current logged in user.



## Usage



## Options

| Flag | Description |
|------|-------------|
| --json | Output in JSON format |

## Examples

### Display current user

Output:


### JSON output

Output:


## Related

- railway login
- railway logout

## Code Examples

railway whoami [OPTIONS]

railway whoami

Logged in as John Doe (john@example.com) ð

railway whoami --json

{
  "name": "John Doe",
  "email": "john@example.com",
  "workspaces": [
    {
      "id": "workspace-id",
      "name": "My Team"
    }
  ]
}



# Projects
Source: https://docs.railway.com/projects

# Project members
Source: https://docs.railway.com/projects/project-members

Learn about the permissions for project members.

<Image src="https://res.cloudinary.com/railway/image/upload/v1644620958/docs/MemberView_New_p0s3be.png"
alt="Screenshot of Project Team Members"
layout="responsive"
width={1377} height={823} quality={100} />

## Scope of permissions

There are three scopes for project members -

1. **Owner**: full administration of the project.

2. **Editor**: Can create deployments, change project settings and add Editor and Viewer members.

   **Note:** Editors can not do destructive actions such as deleting services or deleting the project itself.

3. **Viewer**: Read only access to the project. Viewers can not make deploys or see environment variables.

The Project Owner is charged for the project's usage.


# Project usage
Source: https://docs.railway.com/projects/project-usage

Learn how users can see the resource usage of their projects.

Users can see the usage of a project under <a href="https://railway.com/workspace/usage" target="_blank">the Usage page</a> within the Workspace settings.

<Image src="https://res.cloudinary.com/railway/image/upload/v1631917786/docs/project-usage_gd43fq.png"
alt="Screenshot of Expanded Project Usage Pane"
layout="intrinsic"
width={491} height={286} quality={80} />

### Billing period usage

This section outlines the current usage within a billing period, as well as any discounts and credits the user has applied to their account.

In addition to the current usage, the user can see their estimated resource usage for the current billing period.

### Usage by project

The chart shows the cumulative usage for the billing period. If you delete a project, Railway will still count the usage towards your total.

The Current and Estimated cost metrics show the current resource usage and the estimated usage by the end of the billing period.


# Workspaces
Source: https://docs.railway.com/projects/workspaces

Learn how you can manage a workspaces within Railway.

For more information, visit the documentation on pricing or <a href="https://railway.com/pricing" target="_blank">railway.com/pricing</a>.

## Creating a workspace

Organizations can create a workspace by heading to the <a href="https://railway.com/new/workspace" target="_blank">Create Workspace</a> page and entering the required information.

## Managing workspaces

You can open your workspace's settings page to manage members and see billing information by clicking the gear icon next to the name of your workspace on the dashboard.

## Inviting members

Under the People tab of the settings page, you can invite members. Adding members to the workspace does not incur any additional seat cost.

There are three roles for Workspace members:

- Admin: Full administration of the Workspace and all Workspace projects
- Member: Access to all Workspace projects
- Deployer: View projects and deploy through commits to repos via GitHub integration.

|                              | Admin | Member | Deployer |
| :--------------------------- | :---: | :----: | :------: |
| Viewing workspace projects   |  âï¸   |   âï¸   |    âï¸    |
| Automatic GitHub deployments |  âï¸   |   âï¸   |    âï¸    |
| CLI deployments              |  âï¸   |   âï¸   |    â    |
| Creating variables           |  âï¸   |   âï¸   |    â    |
| Modifying variables          |  âï¸   |   âï¸   |    â    |
| Deleting variables           |  âï¸   |   âï¸   |    â    |
| Modifying service settings   |  âï¸   |   â   |    â    |
| Creating services            |  âï¸   |   âï¸   |    â    |
| Deleting services            |  âï¸   |   â   |    â    |
| Viewing logs                 |  âï¸   |   âï¸   |    â    |
| Creating volumes             |  âï¸   |   âï¸   |    â    |
| Deleting volumes             |  âï¸   |   â   |    â    |
| Creating new projects        |  âï¸   |   âï¸   |    â    |
| Deleting projects            |  âï¸   |   â   |    â    |
| Adding additional members    |  âï¸   |   â   |    â    |
| Removing members             |  âï¸   |   â   |    â    |
| Changing member roles        |  âï¸   |   â   |    â    |
| Adding trusted domains       |  âï¸   |   â   |    â    |
| Making a withdrawal          |  âï¸   |   â   |    â    |
| Accessing billing settings   |  âï¸   |   â   |    â    |
| Accessing audit logs         |  âï¸   |   â   |    â    |

_Note:_ Changes that trigger a deployment will skip the approval requirement when the author has a Deployer role (or higher) and their GitHub account is connected.

## Trusted domains

Trusted Domains let you automatically onboard new members to your workspace. When a Railway user signs up with an email address matching one of your trusted domains, they're added to your workspace with the assigned role.

For example, users signing up with @railway.com are automatically added to the workspace that has railway.com as a trusted domain.

<Image 
  src="https://res.cloudinary.com/railway/image/upload/v1733955730/docs/trusted-domains_oaqfgt.png"
  width="1528"
  height="898"
  alt="Trusted domains are configurable via the workspace settings"
/>

### Verifying a trusted domain

Before adding a Trusted Domain, you must verify ownership by adding your email domain as a custom domain on a Railway service.

You can verify a parent domain using a subdomain. For example, adding verify.example.com as a custom domain allows you to add example.com as trusted domain.

If you don't already have a service using your domain, you can set up a temporary service to verify your domain:

1. Create a new **empty service** in any project (a temporary new project works fine).
2. **Deploy** the service.
3. Open the service and go to the **Settings** tab.
4. Scroll to **Networking -> Custom Domain**.
5. **Add your email domain** (or a subdomain). Leave the port field empty.
6. Click **Add Domain** and follow the DNS setup instructions. If you use Cloudflare or a similar provider, make sure to **disable the proxy**.
7. Wait until the domain is verified.
8. Go to the <a href="https://railway.com/workspace/people" target="_blank">**Trusted Domain settings**</a> and add your email domain. Assign the default role for new members.
9. After the domain is verified and added, you can safely remove the temporary service and DNS record.

Additional notes and troubleshooting:

- You can verify a trusted domain by adding a subdomain (e.g., add verify.example.com as custom domain and use example.com as trusted domain).
- Opening the domain in your browser can speed up verification.
- Trusted Domains are only verified when added. Once verified, the custom domain and its DNS record can be removed safely.

## Transferring projects

Transfer projects from another Workspace or Hobby workspace easily. Detailed instructions can be found here.

## Invoicing and billing

Railway offers a consumption-based pricing model for your projects. You don't get charged for resources you don't use, instead, Railway charges by the minute for each vCPU and memory resource your service uses.

However, if you expect to use a consistent amount of resources for large companies, you can contact us for a quote and demo. Railway will work with you to find a solution that works for your needs. We are willing to offer Purchase Orders and concierge onboarding for large companies.

### Committed spend tiers

Railway offers committed spend tiers for customers with consistent usage needs. Instead of negotiated contract pricing, customers can commit to a specific monthly threshold to unlock additional features and services.

Monthly thresholds for addons is found in the committed spend pricing.

Reach out to us at team@railway.com for more information.



# Build & deploy
Source: https://docs.railway.com/build & deploy

# Services
Source: https://docs.railway.com/services

Discover the different types of services available in your Railway projects.

Each service keeps a log of deployment attempts and performance metrics.

Variables, source references (e.g. GitHub repository URI), and relevant start and build commands are also stored in the service, among other configuration.

_As you create and manage your services, your changes will be collected in a set of staged changes that you must review and deploy, in order to apply them._

## Types of services

#### Persistent services

Services that are always running. Examples include web applications, backend APIs, message queues, database services, etc.

#### Scheduled jobs

Services that are run until completion, on a defined schedule, also called Cron Jobs.

## Creating a service

Create a service by clicking the New button in the top right corner of your project canvas, or by typing new service from the **command palette**, accessible via CMD + K (Mac) or Ctrl + K(Windows).

<Image src="https://res.cloudinary.com/railway/image/upload/v1656640995/docs/CleanShot_2022-06-30_at_18.17.31_cl0wlr.gif"
alt="GIF of the Services view"
layout="responsive"
width={370} height={300} quality={100} />

Services on Railway can be deployed from a GitHub repository, a local directory, or a Docker image.

## Accessing service settings

To access a service's settings, simply click on the service tile from your project canvas and go to the Settings tab.

## Service source

A service source can be any of the following - Docker Image, GitHub or Local repository.

If a Dockerfile is found within the source repository, Railway will automatically use it to build an image for the service.

If you've created an empty service, or would like to update the source for a deployed service, you can do so in the Service settings.

Click on the service, go to the Settings tab, and find the **Service Source** setting.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743121798/docs/deployment-source_sir4mo.png"
alt="Screenshot of how to connect a service to a GitHub repo or Docker image"
layout="responsive"
width={1200} height={421} quality={80} />

### Deploying from a GitHub repo

Define a GitHub repository as your service source by selecting Connect Repo and choosing the repository you'd like to deploy.

When a new commit is pushed to the linked branch, Railway will automatically build and deploy the new code.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743121857/docs/github-repo_z8qkst.png"
alt="Screenshot of a GitHub deployment trigger"
layout="responsive"
width={1200} height={371} quality={80} />

You must link your Railway account to GitHub, to enable Railway to connect to your GitHub repositories. <a href="https://github.com/apps/railway-app/installations/new" target="_blank">You can configure the Railway App in GitHub by clicking this link.</a>

### Deploying a public Docker image

To deploy a public Docker image, specify the path of the image when prompted in the creation flow.

Railway can deploy images from <a href="https://hub.docker.com/" target="_blank">Docker Hub</a>, <a href="https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry" target="_blank">GitHub Container Registry</a>, <a href="https://quay.io/" target="_blank">Quay.io</a>, or <a href="https://docs.gitlab.com/ee/user/packages/container_registry/">GitLab Container Registry</a>. Example paths -

Docker Hub:

- bitnami/redis

GitHub Container Registry:

- ghcr.io/railwayapp-templates/postgres-ssl:latest

GitLab Container Registry:

- registry.gitlab.com/gitlab-cicd15/django-project

Microsoft Container Registry:

- mcr.microsoft.com/dotnet/aspire-dashboard

Quay.io:

- quay.io/username/repo:tag

### Updating Docker images

Railway automatically monitors Docker images for new versions. When an update is available, an update button appears in your service settings. If your image tag specifies a version (e.g., nginx:1.25.3), updating will stage the new version tag. For tags without versions (e.g., nginx:latest), Railway redeploys the existing tag to pull the latest image digest.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1757369631/docs/screenshot-2025-09-08-18.09.17_rkxbqa.png"
alt="Screenshot of a Docker image update button"
layout="responsive"
width={681} height={282} quality={100} />

To enable automatic updates, configure the update settings in your service. You can specify an update schedule and maintenance window. Note that automatic updates trigger a redeployment, which may cause brief downtime (typically under 2 minutes) for services with attached volumes.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1757369630/docs/screenshot-2025-09-08-18.12.09_u2jiz4.png"
alt="Screenshot of a auto update configuration"
layout="responsive"
width={836} height={684} quality={100} />

### Deploying a private Docker image

<Banner variant="info">
Private Docker registry deployments require the Pro plan.
</Banner>

To deploy from a private Docker registry, specify the path of the image when prompted in the creation flow, as well as authentication credentials (username, password) to the registry.

<Image src="https://res.cloudinary.com/railway/image/upload/v1743197249/docs/source-image_gn52ff.png"
alt="GIF of the Services view"
layout="intrinsic"
width={1200} height={746} quality={100} />

If deploying an image from <a href="https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry" target="_blank">GitHub Container Registry</a>, provide a <a href="https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-to-the-container-registry" target="_blank">personal access token (classic)</a>.

### Deploying from a local directory

Use the CLI to deploy a local directory to a service -

1. Create an Empty Service by choosing Empty Service during the service creation flow.
2. In a Terminal, navigate to the directory you would like to deploy.
3. Link to your Railway project using the railway link CLI command.
4. Deploy the directory using railway up. The CLI will prompt you to choose a service target, be sure to choose the empty service you created.

## Deploying a monorepo

For information on how to deploy a Monorepo click here.

## Ephemeral storage

Every service deployment has access to ephemeral storage, with the limits being 1GB on the Free plan and 100GB on a paid plan. If a service deployment consumes more than its ephemeral storage limit, it can be forcefully stopped and redeployed.

If your service requires data to persist between deployments, or needs more storage, you should add a volume.

## Monitoring

Logs, metrics, and usage information is available for services and projects. Check out the observability guides for information on how to track this data.

## Changing the service icon

Customize your project canvas for easier readability by changing the service icon.

1. Right click on the service
2. Choose Update Info
3. Choose Icon
4. Begin typing to see a list of available icons, pulled from the <a href="https://devicons.railway.com/" target="_blank">devicons</a> service.

You can also access this configuration from the command palette.

## Approving a deployment

If a member of a GitHub repo doesn't have a linked Railway account. Railway by default will not deploy any pushes to a connected GitHub branch within Railway.

Railway will then create a Deployment Approval within a Service prompting a user to determine if they want to deploy their commit or not.

<Image src="https://res.cloudinary.com/railway/image/upload/v1724222405/CleanShot_2024-08-21_at_02.38.25_2x_vxurvb.png"
alt="screenshot of the deployment approval ui"
layout="responsive"
width={874} height={302} quality={100} />

Deploy the queued deployment by clicking the "Approve" button. You can dismiss the request by clicking the three dots menu and clicking "Reject".

## Templates

A template is a pre-configured group of services. A template can be used to start a project or to expand an existing project.

## Constraints

- Service names have a max length of 32 characters.

## Deleting a service

Delete a service by opening the project's settings and scrolling to the danger section.


# Environments
Source: https://docs.railway.com/environments

Manage complex development workflows via environments in your projects on Railway.



## How it works

All projects in Railway are created with a production environment by default. Once a project has been created, new environments can be created and configured to complement any development workflow.

All changes made to a service are scoped to a single environment. This means that you can make changes to a service in an environment without affecting other environments.

## Types of environments

### Persistent environments

Persistent environments are intended to persist but remain isolated from production with regard to their configuration.

For example, it is a common pattern to maintain a staging environment that is configured to auto-deploy from a staging branch and with variables relevant to staging.

### PR environments

PR Environments are temporary. They are created when a Pull Request is opened on a branch and are deleted as soon as the PR is merged or closed.

## Use cases

Environments are generally used for isolating changes from the production environment, to iterate and test before pushing to production.

- Have development environments for each team member that are identical to the production environment
- Have separate staging and production environments that auto-deploy when changes are made to different branches in a code repository.

## Create an environment

1. Select + New Environment from the environment drop down in the top navigation. You can also go to Settings > Environments.
2. Choose which type of environment to create -

   - **Duplicate Environment** creates a copy of the selected environment, including services, variables, and configuration.

     When the duplicate environment is created, all services and their configuration will be staged for deployment.
     _You must review and approve the staged changes before the services deploy._

   - **Empty Environment** creates an empty environment with no services.

## Sync environments

You can easily sync environments to _import_ one or more services from one environment into another environment.

1. Ensure your current environment is the one that should _receive_ the synced service(s)
2. Click Sync at the top of the canvas
3. Select the environment from which to sync changes
4. Upon sync, each service card that has received a change will be tagged "New", "Edited", "Removed"
5. Review the staged changes by clicking Details on the staged changes banner
6. Click "Deploy" once you are ready to apply the changes and re-deploy

<Image src="https://res.cloudinary.com/railway/image/upload/v1743192480/docs/sync-environments_sujrxq.png"
            alt="Staged changes on Railway canvas"
            layout="responsive"
            width={1200} height={843} quality={100} />

## PR environments

Railway can spin up a temporary environment whenever you open a Pull Request. To enable PR environments, go to your Project Settings -> Environments tab.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1699568846/docs/enablePrEnv_f5n2hx.png"
alt="Screenshot of Deploy Options"
layout="responsive"
width={1622} height={506} quality={80} />

When enabled, a temporary environment is spun up to support the Pull Request deploy. These environments are deleted as soon as these PRs are merged or closed.

### How come my GitHub PR won't deploy?

Railway will not deploy a PR branch from a user who is not in your workspace or invited to your project without their associated GitHub account.

### Domains in PR environments

To enable automatic domain provisioning in PR environments, ensure that services in your base environment use Railway-provided domains. Services in PR environments will only receive domains automatically when their corresponding base environment services have Railway-provided domains.

### Focused PR environments

<PriorityBoardingBanner />

For monorepos and multi-service projects, Focused PR Environments only deploy services affected by files changed in the pull request. This speeds up PR environments and reduces resource usage.

#### How it works

When a PR is opened, Railway determines which services to deploy:

1. Services connected to the PR repo that are affected by changed files (based on watch paths or root directory)
2. Dependencies of affected services (via variable references like ${{service.URL}})

All other services are skipped and indicated on the canvas. The GitHub PR comment shows which services were skipped.

#### Deploying skipped services

Skipped services can be deployed manually from the canvas. Click on the skipped service and select "Deploy" to add it to the PR environment.

#### Enabling focused PR environments

1. Go to **Project Settings â Environments**
2. Ensure PR Environments are enabled
3. Toggle **Enable Focused PR Environments**

### Bot PR environments

You can enable automatic PR environment creation for PRs opened by GitHub bots using the Enable Bot PR Environments toggle on the Environments tab in the Project Settings page.

This works with any GitHub bot, including Dependabot, Renovate, GitHub Copilot, Claude Code, Devin, Jules, and more.

<Image
  src="https://res.cloudinary.com/railway/image/upload/v1768408949/docs/guides/environments/mockup-1768408821891_wxdyrr.png"
  alt="Bot PR Environments toggle"
  layout="responsive"
  width={3096}
  height={940}
  quality={80}
/>

## Environment RBAC

<Banner variant="info">
Environment RBAC is available on Railway Enterprise.
</Banner>

Restrict access to sensitive environments like production. Non-admin members can see these environments exist but cannot access their resources (variables, logs, metrics, services, and configurations). They can still trigger deployments via git push.

| Role | Can access | Can toggle |
| :--- | :---: | :---: |
| Admin | âï¸ | âï¸ |
| Member | â | â |
| Deployer | â | â |

For detailed setup instructions and best practices, see the Environment RBAC guide.

## Forked environments (deprecated)

As of January 2024, forked environments have been deprecated in favor of Isolated Environments with the ability to Sync.

Any environments forked prior to this change will remain, however, you must adopt the Sync Environments flow, in order to merge changes into your base environment.

## Troubleshooting

Having issues with environments? Check out the Troubleshooting guide or reach out on Central Station.


# Reference
Source: https://docs.railway.com/variables/reference

Reference documentation for Railway variables, including template syntax and all available system variables.

Railway's templating syntax gives you flexibility in managing variables:

- NAMESPACE - The value for NAMESPACE is determined by the location of the variable being referenced. For a shared variable, the namespace is "shared". For a variable defined in another service, the namespace is the name of the service, e.g. "Postgres" or "backend-api".
- VAR - The value for VAR is the name, or key, of the variable being referenced.

You can also combine additional text or even other variables, to construct the values that you need:

## Variable functions

Template variable functions allow you to dynamically generate variables (or parts of a variable) on demand when the template is deployed.

## Railway-provided variables

Railway provides the following additional system environment variables to all
builds and deployments.

| Name                           | Description                                                                                                                                          |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| RAILWAY_PUBLIC_DOMAIN        | The public service or customer domain, of the form example.up.railway.app                                                                          |
| RAILWAY_PRIVATE_DOMAIN       | The private DNS name of the service.                                                                                                                 |
| RAILWAY_TCP_PROXY_DOMAIN     | (see TCP Proxy for details) The public TCP proxy domain for the service, if applicable. Example: roundhouse.proxy.rlwy.net |
| RAILWAY_TCP_PROXY_PORT       | (see TCP Proxy for details) The external port for the TCP Proxy, if applicable. Example: 11105                             |
| RAILWAY_TCP_APPLICATION_PORT | (see TCP Proxy for details) The internal port for the TCP Proxy, if applicable. Example: 25565                             |
| RAILWAY_PROJECT_NAME         | The project name the service belongs to.                                                                                                             |
| RAILWAY_PROJECT_ID           | The project id the service belongs to.                                                                                                               |
| RAILWAY_ENVIRONMENT_NAME     | The environment name of the service instance.                                                                                                        |
| RAILWAY_ENVIRONMENT_ID       | The environment id of the service instance.                                                                                                          |
| RAILWAY_SERVICE_NAME         | The service name.                                                                                                                                    |
| RAILWAY_SERVICE_ID           | The service id.                                                                                                                                      |
| RAILWAY_REPLICA_ID           | The replica ID for the deployment.                                                                                                                   |
| RAILWAY_REPLICA_REGION       | The region where the replica is deployed. Example: us-west2                                                                                        |
| RAILWAY_DEPLOYMENT_ID        | The ID for the deployment.                                                                                                                           |
| RAILWAY_SNAPSHOT_ID          | The snapshot ID for the deployment.                                                                                                                  |
| RAILWAY_VOLUME_NAME          | The name of the attached volume, if any. Example: foobar                                                                                           |
| RAILWAY_VOLUME_MOUNT_PATH    | The mount path of the attached volume, if any. Example: /data                                                                                      |

### Git variables

These variables are provided if the deploy originated from a GitHub trigger.

| Name                         | Description                                                                                                                                                                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RAILWAY_GIT_COMMIT_SHA     | The git SHA of the commit that triggered the deployment. Example: d0beb8f5c55b36df7d674d55965a23b8d54ad69b |
| RAILWAY_GIT_AUTHOR         | The user of the commit that triggered the deployment. Example: gschier                                                                                                                             |
| RAILWAY_GIT_BRANCH         | The branch that triggered the deployment. Example: main                                                                                                                                            |
| RAILWAY_GIT_REPO_NAME      | The name of the repository that triggered the deployment. Example: myproject                                                                                                                       |
| RAILWAY_GIT_REPO_OWNER     | The name of the repository owner that triggered the deployment. Example: mycompany                                                                                                                 |
| RAILWAY_GIT_COMMIT_MESSAGE | The message of the commit that triggered the deployment. Example: Fixed a few bugs                                                                                                                 |

### User-provided configuration variables

Users can use the following environment variables to configure Railway's behavior.

| Name                                  | Description                                                                                                                                                                   |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RAILWAY_DEPLOYMENT_OVERLAP_SECONDS  | How long the old deploy will overlap with the newest one being deployed, its default value is 0. Example: 20                                                              |
| RAILWAY_DOCKERFILE_PATH             | The path to the Dockerfile to be used by the service, its default value is Dockerfile. Example: Railway.dockerfile                                                        |
| RAILWAY_HEALTHCHECK_TIMEOUT_SEC     | The timeout length (in seconds) of healthchecks. Example: 300                                                                                                               |
| RAILWAY_DEPLOYMENT_DRAINING_SECONDS | The SIGTERM to SIGKILL buffer time (in seconds), its default value is 0. Example: 30                                                                                        |
| RAILWAY_RUN_UID                     | The UID of the user which should run the main process inside the container. Set to 0 to explicitly run as root.                                                             |
| RAILWAY_SHM_SIZE_BYTES              | This variable accepts a value in binary bytes, with a default value of 67108864 bytes (64 MB)                                                                                 |

## Code Examples

${{NAMESPACE.VAR}}

DOMAIN=${{shared.DOMAIN}}
GRAPHQL_PATH=/v1/gql
GRAPHQL_ENDPOINT=https://${{DOMAIN}}/${{GRAPHQL_PATH}}


# Cron jobs
Source: https://docs.railway.com/cron-jobs

Learn how to run cron jobs on Railway.

Services configured as cron jobs are expected to execute a task, and terminate as soon as that task is finished, leaving no open resources.

## How it works

Railway will look for a defined cron schedule in your service settings, and execute the start command for that service on the given schedule. The service is expected to execute a task, and exit as soon as that task is finished, not leaving any resources open, such as database connections.

#### Scheduling libraries

If you are already using a scheduling library or system in your service such as node-cron or Quartz, Railway cron jobs are a substitute of them that allows you to save resources between executions.

## Configuring a cron job

To configure a cron job:

1. Select a service and go to the Settings section.
2. Within "Cron Schedule", input a crontab expression.
3. Once the setting is saved, the service will run according to the cron schedule.

## Service execution requirements

Scheduled services should exit as soon as they are done with the task they are responsible to perform. Thus, the process should close any connections, such as database connections, to exit properly.

Currently, Railway does not automatically terminate deployments. As a result, if a previous execution is still running when the next scheduled execution is due, Railway will skip the new cron job.

### Why isn't my cron running as scheduled?

An important requirement of a service that runs as a Cron, is that it terminates on completion and leaves no open resources. If the code that runs in your Cron service does not exit, subsequent executions of the Cron will be skipped.

If you see that a previous execution of your Cron service has a status of Active, the execution is still running and any new executions will not be run.

## Crontab expressions

A crontab expression is a scheduling format used in Unix-like operating systems to specify when and how often a command or script should be executed automatically.

Crontab expressions consists of five fields separated by spaces, representing different units of time. These fields specify the minute, hour, day of the month, month, and day of the week when the command should be executed.

The values of these fields can be an asterisk *, a list of values separated by commas, a range of values (using -), step values (using /) or an integer value.

#### Field definitions

- **Minute (0-59)**: Represents the minute of the hour when the command should be executed. An asterisk (*) denotes any value, meaning the command will be executed every minute, or you can specify a specific minute value (e.g., 0, 15, 30).

- **Hour (0-23)**: Represents the hour of the day when the command should be executed. You can specify a specific hour value (e.g., 0, 6, 12), or use an asterisk (*) to indicate any hour.

- **Day of the month (1-31)**: Represents the day of the month when the command should be executed. You can specify a specific day value (e.g., 1, 15, 31), or use an asterisk (*) to indicate any day.

- **Month (1-12)**: Represents the month when the command should be executed. You can specify a specific month value (e.g., 1, 6, 12), or use an asterisk (*) to indicate any month.

- **Day of the week (0-7, where both 0 and 7 represent Sunday)**: Represents the day of the week when the command should be executed. You can specify a specific day value (e.g., 0-Sunday, 1-Monday, etc.), or use an asterisk (*) to indicate any day of the week.

Note that schedules are based on UTC (Coordinated Universal Time).

## Frequency

The shortest time between successive executions of a cron job cannot be less than 5 minutes.

## Examples

- Run a command every hour at the 30th minute: 30 * * * *

- Run a command every day at 3:15 PM: 15 15 * * *

- Run a command every Monday at 8:00 AM: 0 8 * * 1

- Run a command every month on the 1st day at 12:00 AM: 0 0 1 * *

- Run a command every Sunday at 2:30 PM in January: 30 14 * 1 0

- Run a command every weekday (Monday to Friday) at 9:30 AM: 30 9 * * 1-5

- Run a command every 15 minutes: */15 * * * *

- Run a command every 2 hours: 0 */2 * * *

- Run a command every 2nd day of the month at 6:00 AM: 0 6 2 * *

## FAQ

### When to use railway's cron jobs?

- For short-lived tasks that complete quickly and exit properly, such as a daily database backup.
- When you want to save resources between task executions, as opposed to having an in-code scheduler run 24/7.

### When not to use railway's cron jobs?

- For long-running processes that don't exit, such as a web server or discord bot.
- When you need more frequent execution than every 5 minutes.
- When you need absolute time precision. Railway does not guarantee execution times to the minute as they can vary by a few minutes.

### What time zone is used for cron jobs?

Cron jobs are scheduled based on UTC (Coordinated Universal Time).

You will need to account for timezone offsets when setting your cron schedule.

## Code Examples

* * * * *
â â â â â
â â â â ââââââââââââ Day of the week (0 - 6)
â â â ââââââââââââââ Month (1 - 12)
â â ââââââââââââââââ Day of the month (1 - 31)
â ââââââââââââââââââ Hour (0 - 23)
ââââââââââââââââââââ Minute (0 - 59)


# Functions
Source: https://docs.railway.com/functions

Write and deploy code from the Railway canvas without managing infrastructure or creating a git repository.

Functions are Services that run a single file of TypeScript code using the Bun runtime.
Use them like any other Service, but without the overhead of a repository.

They are ideal for small tasks like handling webhooks, cron jobs, or simple APIs.

## Key features

- **Instant deploys**: Deploy code changes _in seconds_. No need to wait for a build step.
- **Import any NPM package**: Use any NPM package in your function. We will automatically install it for you when your code runs. Pin specific versions by using a package@version syntax in your imports, e.g. import { Hono } from "hono@4"
- **Use native Bun APIs**: Access Bun APIs like Bun.file() and Bun.serve().
- **Service variables**: Service Variables are automatically available in the function editor via import.meta.env, process.env, or Bun.env
- **Attach volumes**: Persist data in your function using Volumes.
- **Use Vim**: Enable Vim keybindings in the function editor by using the shortcut Ctrl+Option+V on a Mac or Ctrl+Alt+V on Windows.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1738958871/docs/railway-functions-2_vk0umf.png"
alt="Screenshot of pre-deploy command configuration"
layout="intrinsic"
width={589} height={366} quality={80} />

## Limitations

- 1 file per function
- Max file size of 96KB

## Edit and deploy

If you're familiar with VSCode or other IDEs, you'll feel right at home with the built-in editor.

- **To edit** your function, open the "Source Code" tab in your service.
- **To stage** your changes, press â+S (or Control+S if using Windows).
- **To deploy** staged changes, press Shift+Enter.

## Versioning

Railway automatically versions your function code. Each time you deploy, a new version is created and is available for rollback.
To rollback or redeploy a previous version, find the Deployment you want to rollback to in the "Deployments" tab
of your service. Then click the "Redeploy" button.

You can find the source code of a previous deployment by opening the deployment details.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1738960017/docs/railway-functions-versions_jqdhal.png"
alt="Screenshot of pre-deploy command configuration"
layout="intrinsic"
width={588} height={499} quality={80} />


# Reference
Source: https://docs.railway.com/config-as-code/reference

Learn how to manage and deploy apps on Railway using config as code with toml and json files.

alongside your code. By default, we will look for a railway.toml or
railway.json file.

Everything in the build and deploy sections of the service
settings can be specified in this configuration file.

## How does it work?

When a new deployment is triggered, Railway will look for any config files in your
code and combine these values with the settings from the dashboard.

The resulting build and deploy config will be used **only for the current deployment**.

The settings in the dashboard will not be updated with the settings defined in
code.

Configuration defined in code will always override values from the
dashboard.

## Config source location

On the deployment details page, all the settings that a deployment went out with are shown. For settings that come from a configuration file, there is a little file icon. Hovering over the icon will show exactly what part of the file the values originated from.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743195106/docs/configuration_emrjth.png"
alt="Screenshot of Deployment Details Pane"
layout="responsive"
width={1200} height={631} quality={100} />

## Configurable settings

### Specify the builder

Set the builder for the deployment.

Possible values are:

- RAILPACK (default)
- DOCKERFILE
Note: Railway will always build with a Dockerfile if it finds one. New services default to Railpack unless otherwise specified.

Read more about Builds here.

### Watch patterns

Array of patterns used to conditionally trigger a deploys.

Read more about watch patterns here.

### Build command

Build command to pass to the builder.

This field can be set to null.

Read more about the build command here.

### Dockerfile path

Location of non-standard Dockerfile.

This field can be set to null.

More about building from a Dockerfile here.

### Railpack version

Must be a valid Railpack version.

This field can be set to null.

You can also use the RAILPACK_VERSION configuration
variable
to set the Railpack version.

### Start command

The command to run when starting the container.

This field can be set to null.

Read more about the start command here.

### Pre-deploy command

The command to run before starting the container.

This field can be omitted.

Read more about the pre-deploy command here.

### Multi-region configuration

Horizontal scaling across multiple regions, with two replicas in each region.

This field can be set to null.

Read more about horizontal scaling with multiple regions here.

### Healthcheck path

Path to check after starting your deployment to ensure it is healthy.

This field can be set to null.

Read more about the healthcheck path here.

### Healthcheck timeout

Number of seconds to wait for the healthcheck path to become healthy.

This field can be set to null.

Read more about the healthcheck timeout here.

### Restart policy type

How to handle the deployment crashing.

Possible values are:

- ON_FAILURE
- ALWAYS
- NEVER

Read more about the Restart policy here.

### Restart policy max retries

Set the max number of retries for the restart policy.

This field can be set to null.

Read more about the Restart policy here.

### cron schedule

Cron schedule of the deployed service.

This field can be set to null.

### Setting environment overrides

Configuration can be overridden for a specific environment by nesting it in a
environments.[name] block.

When resolving the settings for a deployment, Railway will use this priority order:

1. Environment specific config in code
2. Base config in code
3. Service settings

The following example changes the start command just in the production
environment.

#### PR environment overrides

Deployments for pull requests can be configured using a special pr environment. This configuration is applied only to deploys that belong to an ephemeral environment. When resolving the settings for a PR deployment, the following priority order is used:

1. Environment with the name of the ephemeral environment
2. Environment with the hardcoded name "pr"
3. Base environment of the pull request
4. Base config as code
5. Service settings

### Deployment teardown

You can configure Deployment Teardown settings to tune the behavior of zero downtime deployments on Railway.

#### Overlap seconds

Time in seconds that the previous deploy will overlap with the newest one being deployed. Read more about the deployment's lifecycle here.

This field can be set to null.

#### Draining seconds

The time in seconds between when the previous deploy is sent a SIGTERM to the time it is sent a SIGKILL. Read more about the deployment's lifecycle here.

This field can be set to null.

## Code Examples

{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "builder": "RAILPACK"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "watchPatterns": ["src/**"]
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "buildCommand": "yarn run build"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "dockerfilePath": "Dockerfile.backend"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "railpackVersion": "0.7.0"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "startCommand": "node index.js"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "preDeployCommand": ["npm run db:migrate"]
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "multiRegionConfig": {
      "us-west2": {
        "numReplicas": 2
      },
      "us-east4-eqdc4a": {
        "numReplicas": 2
      },
      "europe-west4-drams3a": {
        "numReplicas": 2
      },
      "asia-southeast1-eqsg3a": {
        "numReplicas": 2
      }
    }
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "healthcheckPath": "/health"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "healthcheckPath": "/health",
    "healthcheckTimeout": 300
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "restartPolicyType": "ALWAYS"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "restartPolicyType": "ALWAYS",
    "restartPolicyMaxRetries": 5
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "cronSchedule": "*/15 * * * *"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "environments": {
    "staging": {
      "deploy": {
        "startCommand": "npm run staging"
      }
    }
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "environments": {
    "pr": {
      "deploy": {
        "startCommand": "npm run pr"
      }
    }
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "overlapSeconds": "60"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "drainingSeconds": "10"
  }
}


# Build configuration
Source: https://docs.railway.com/builds/build-configuration

Learn how to configure Railpack, optimize build caching, and set up watchpaths.



## Railpack

Railway uses <a href="https://railpack.com" target="_blank">Railpack</a> to
build your code. It works with zero configuration, but can be customized using
environment variables or a config
file. Configuration options include:

- Language versions
- Build/install/start commands
- Mise and Apt packages to install
- Directories to cache

For a full list of configuration options, please view the <a
href="https://railpack.com/config/environment-variables"
target="_blank">Railpack docs</a>. You can find a complete list of languages we
support out of the box here.

## Customize the build command

You can override the detected build command by setting a value in your service
settings. This is run after languages and packages have been installed.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743192207/docs/build-command_bwdprb.png"
alt="Screenshot of Railway Build Command"
layout="responsive"
width={1200} height={373} quality={80} />

## Set the root directory

The root directory defaults to / but can be changed for various use-cases like
monorepo projects.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743192841/docs/root-directory_nfzkfi.png"
alt="Screenshot of Root Directory"
layout="responsive"
width={1200} height={421} quality={80} />

When specified, all build and deploy
commands will operate within the defined root directory.

**Note:** The **Railway Config File** does not follow the **Root Directory** path. You have to specify the absolute path for the railway.json or railway.toml file, for example: /backend/railway.toml

## Configure watch paths

Watch paths are <a href="https://git-scm.com/docs/gitignore#_pattern_format" target="_blank">gitignore-style</a> patterns
that can be used to trigger a new deployment based on what file paths have
changed.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743192841/docs/watch-paths_zv62py.png"
alt="Screenshot of Railway Watch Paths"
layout="responsive"
width={1200} height={456} quality={80} />

For example, a monorepo might want to only trigger builds if files are
changed in the /packages/backend directory.

When specified, any changes that
don't match the patterns will skip creating a new deployment. Multiple patterns
can be combined, one per line.

_Note, if a Root Directory is provided, patterns still operate from /. For a root directory of /app, /app/**.js would be used as a pattern to match files in the new root._

Here are a few examples of common use-cases:

_Note, negations will only work if you include files in a preceding rule._

## Install specific packages using Railpack

| Environment variable            | Description                                                    |
|---------------------------------|----------------------------------------------------------------|
| RAILPACK_PACKAGES             | A list of Mise packages to install    |
| RAILPACK_BUILD_APT_PACKAGES   | Install additional Apt packages during build                   |
| RAILPACK_DEPLOY_APT_PACKAGES  | Install additional Apt packages in the final image             |

See the Railpack docs for more information.

## Procfiles

Railpack automatically detects commands defined in
Procfiles. Although this is not
recommended and specifing the start command directly in your service settings is
preferred.

## Specify a custom install command

You can override the install command by setting the RAILPACK_INSTALL_COMMAND
environment variable in your service settings.

## Disable build layer caching

By default, Railway will cache build layers to provide faster build times. If
you have a need to disable this behavior, set the following environment variable
in your service:

## Why isn't my build using cache?

Since Railway's build system scales up and down in response to demand, cache hit
on builds is not guaranteed.

If you have a need for faster builds and rely on build cache to satisfy that
requirement, you should consider creating a pipeline to build your own image and
deploy your image directly.

## Code Examples

# Match all TypeScript files under src/
/src/**/*.ts

# Match Go files in the root, but not in subdirectories
/*.go

# Ignore all markdown files
**
!/*.md

NO_CACHE=1


# Build and start commands
Source: https://docs.railway.com/builds/build-and-start-commands

Learn how to configure build and start commands.

If necessary, build and start commands can be manually configured.

## How it works

Overrides are exposed in the service configuration to enable customizing the Build and Start commands. When an override is configured, Railway uses the commands specified to build and start the service.

#### Build command

The command to build the service, for example yarn run build. Override the detected build command by setting a value in your service settings.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743192207/docs/build-command_bwdprb.png"
alt="Screenshot of Railway Build Command"
layout="responsive"
width={1200} height={373} quality={80} />

#### Start command

Railway automatically configures the start command based on the code being deployed.

If your service deploys with a Dockerfile or from an image, the start command defaults to the ENTRYPOINT and / or CMD defined in the Dockerfile.

Override the detected start command by setting a value in your service settings.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1637798815/docs/custom-start-command_a8vcxs.png"
alt="Screenshot of custom start command configuration"
layout="intrinsic"
width={1302} height={408} quality={80} />

If you need to use environment variables in the start command for services deployed from a Dockerfile or image you will need to wrap your command in a shell -

This is because commands ran in exec form do not support variable expansion.

## Support

For more information on how to configure builds, check out the Builds guide section.

For more information on how to configure a service's deployment lifecycle, like the Start command, check out the Deployments guide section.

## Code Examples

/bin/sh -c "exec python main.py --port $PORT"


# Dockerfiles
Source: https://docs.railway.com/builds/dockerfiles

Learn Dockerfile configuration on Railway.



## How it works

When building a service, Railway will look for and use a Dockerfile at the root of the source directory.

**Note:** For the automatic Dockerfile detection to work, the Dockerfile must be named Dockerfile with a capital D, otherwise Railway will not use it by default.

Railway notifies you when it's using the Dockerfile in the build process with the following message in the logs:

## Custom Dockerfile path

By default, we look for a file named Dockerfile in the root directory. If you want to use a custom filename or path, you can set a variable defining the path.

In your service variables, set a variable named RAILWAY_DOCKERFILE_PATH to specify the path to the file.

For example, if your Dockerfile was called Dockerfile.origin, you would specify it like this:

If your Dockerfile is in another directory, specify it like this:

### Use config as Code

You can also set your custom Dockerfile path using config as code.

## Using variables at build time

If you need to use the environment variables that Railway injects at build time, which include variables that you define and Railway-provided variables, you must specify them in the Dockerfile using the ARG command.

For example:

Be sure to declare your environment variables in the stage they are required in:

## Cache mounts

Railway supports cache mounts in your Dockerfile in the following format:

Replace <service id> with the id of the service. 

<Banner variant="info">
    Environment variables can't be used in cache mount IDs, since that is invalid syntax.
</Banner>

### Target path

Unsure of what your target path should be? Check your language or runtime's documentation for the default cache directory path.

**Example**

For Python, the PIP_CACHE_DIR is /root/.cache/pip.

So the mount command is specified like this:

## Docker compose

You can import services straight from your Docker Compose file! Just drag and drop your Compose file onto your project canvas, and your services (and any mounted volumes) will be auto-imported as staged changes. It's like magic, but with YAML instead of wands. ðª

A quick heads-up: we don't support every possible Compose config just yet (because Rome wasn't built in a day). But don't worry, we're on it!

## Code Examples

==========================
Using detected Dockerfile!
==========================

RAILWAY_DOCKERFILE_PATH=Dockerfile.origin

RAILWAY_DOCKERFILE_PATH=/build/Dockerfile

# Specify the variable you need
ARG RAILWAY_SERVICE_NAME
# Use the variable
RUN echo $RAILWAY_SERVICE_NAME

FROM node

ARG RAILWAY_ENVIRONMENT

--mount=type=cache,id=s/<service id>-<target path>,target=<target path>

--mount=type=cache,id=s/<service id>-/root/cache/pip,target=/root/.cache/pip


# Private registries
Source: https://docs.railway.com/builds/private-registries

Learn how to deploy Docker images from private container registries on Railway.



## Supported registries

Any registry that supports standard Docker authentication works with Railway. Here are a few:

| Registry | Domain |
| -------- | ------ |
| Docker Hub | docker.io (default) |
| GitHub Container Registry | ghcr.io |
| GitLab Container Registry | registry.gitlab.com |
| Quay.io | quay.io |
| AWS ECR Public | public.ecr.aws |
| Google Artifact Registry | us-west1-docker.pkg.dev |
| Microsoft Container Registry | mcr.microsoft.com |

## Requirements

Private registry credentials are available on the **Pro plan**. If you're on a Free, Trial, or Hobby plan, you'll need to upgrade to use private registries.

## Configure registry credentials

To deploy from a private registry:

1. Navigate to your service's **Settings** page
2. Under the **Source** section, locate **Registry Credentials**
3. Enter your credentials and save

<video src="https://res.cloudinary.com/railway/video/upload/v1767657773/AddCredentials_dkhoyx.mp4" controls autoplay loop muted playsinline/>

### GitHub container registry (GHCR)

For images hosted on ghcr.io, Railway provides a simplified authentication flow:

1. Create a GitHub Personal Access Token with the read:packages scope
2. Enter your token in the **GitHub Access Token** field

Railway automatically handles the username configuration for GHCR.

### Other registries

For all other registries, provide:

| Field | Description |
| ----- | ----------- |
| **Username** | Your registry username or service account name/id |
| **Password** | Your registry password, access token, or API key |

The exact credentials depend on your registry provider:

- **Docker Hub** - Docker ID and personal access token
- **GitLab** - Username and personal access token with read_registry scope (add write_registry for push access)
- **Quay.io** - Robot account username in format namespace+robotname and the generated robot token
- **AWS ECR** - Use AWS as username and an authentication token as password, generated via aws ecr get-login-password (tokens expire after 12 hours)
- **Google Artifact Registry** - Use _json_key as username and your service account JSON key contents as password

## Security

Registry credentials are encrypted at rest using envelope encryption. Credentials are only decrypted at deployment time when pulling your image.

## Image format

When specifying a private image, use the full image path including the registry domain:

For Docker Hub private images, you can omit the domain:

## Code Examples

ghcr.io/your-org/your-image:tag
registry.gitlab.com/your-group/your-project:tag
your-dockerhub-username/private-repo:tag

your-username/private-image:latest


# Railpack
Source: https://docs.railway.com/builds/railpack

Railway uses Railpack to build and deploy your code with zero configuration.

build and deploy your code with zero configuration.

## Supported languages

Currently, we support the following languages out of the box:

- Node
- Python 
- Go
- PHP
- HTML/Staticfile
- Java
- Ruby
- Deno
- Rust
- Elixir
- Shell scripts

## How it works

Railpack automatically analyzes your code and turns it into a container image.
It detects your programming language, installs dependencies, and configures
build and start commands without any manual configuration required.

## The build process

When Railway builds your app with Railpack, the build process will
automatically:

1. **Analyze** your source code to detect the programming language and framework
2. **Install** the appropriate runtime and dependencies
3. **Build** your application using detected or configured build commands
4. **Package** everything into an optimized container image

## Configuration

Railpack works with zero configuration, but you can customize the build process
when needed using environment variables
or a Railpack config file.

## Support

If you have a language or feature that you want us to support, please don't
hesitate to reach out on <a href="https://discord.gg/xAm2w6g"
target="_blank">Discord</a> or on the <a
href="https://github.com/railwayapp/railpack">Railpack repo</a>.


# Pre-deploy command
Source: https://docs.railway.com/deployments/pre-deploy-command

Learn how to execute commands between building and deploying your application.

They execute within your private network and have access to your application's environment variables.

If your command fails, it will not be retried and the deployment will not proceed.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1736533539/docs/pre-deploy-command_sp1zqh.png"
alt="Screenshot of pre-deploy command configuration"
layout="intrinsic"
width={1494} height={644} quality={80} />

For pre-deploy commands to work correctly, ensure that:

- It exits with a status code of 0 to indicate success or non-zero to indicate failure.
- It runs in a reasonable amount of time. It will occupy a slot in your build queue.
- It does not rely on the application running.
- It has the dependencies it needs to run installed in the application image.
- It does not attempt to read or write data to the volume or filesystem, that should instead be done as part of the start command.

<Banner variant="warning">Pre-deploy commands execute in a separate container from your application. Changes to the filesystem are not persisted and volumes are not mounted.</Banner>


# Start command
Source: https://docs.railway.com/deployments/start-command

Learn how to set up a start command in your service to run your deployments on Railway.

Railway automatically configures the start command based on the code being
deployed, see Build and Start Commands for more details

## Configure the start command

When necessary, start commands may be overridden, like for advanced use-cases such as deploying multiple projects from a single monorepo.

When specifying a start command, the behavior depends on the type of deployment:

- **Dockerfile / Image**: the start command overrides the image's ENTRYPOINT in <a href="https://docs.docker.com/reference/dockerfile/#shell-and-exec-form" target="_blank">exec form</a>.

  If you need to use environment variables in the start command for services deployed from a Dockerfile or image you will need to wrap your command in a shell -

  This is because commands ran in exec form do not support variable expansion.

- **Railpack**: the start command is ran in a shell process.

  This supports the use of environment variables without needing to wrap your command in a shell.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1637798815/docs/custom-start-command_a8vcxs.png"
alt="Screenshot of custom start command configuration"
layout="intrinsic"
width={1302} height={408} quality={80} />

## Dockerfiles & images

If your service deploys with a Dockerfile or from an image, the start command defaults to the ENTRYPOINT and / or CMD defined in the Dockerfile.

## Code Examples

/bin/sh -c "exec python main.py --port $PORT"


# Deployment actions
Source: https://docs.railway.com/deployments/deployment-actions

Explore the full range of actions available on the Service Deployments tab to manage your deployments.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1645148376/docs/deployment-photo_q4q8in.png"
alt="Screenshot of Deploy View"
layout="responsive"
width={1103} height={523} quality={80} />

## Rollback

Rollback to previous deployments if mistakes were made. To perform a rollback, click the three dots at the end of a previous deployment, you will then be asked to confirm your rollback.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1645149734/docs/rollback_mhww2u.png"
alt="Screenshot of Rollback Menu"
layout="responsive"
width={1518} height={502} quality={80} />

A deployment rollback will revert to the previously successful deployment. Both the Docker
image and custom variables are restored during the rollback process.

_Note: Deployments older than your plan's retention policy cannot be restored via rollback, and thus the rollback option will not be visible._

## Redeploy

A successful, failed, or crashed deployment can be re-deployed by clicking the three dots at the end of a previous deployment.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1666380373/docs/redeploy_ghinkb.png"
alt="Screenshot of Redeploy Menu"
layout="responsive"
width={888} height={493} quality={100} />

This will create an new deployment with the exact same code and build/deploy configuration.

_Note: To trigger a deployment from the latest commit, use the Command Palette: CMD + K -> "Deploy Latest Commit". This will deploy the latest commit from the **Default** branch in GitHub._

_Currently, there is no way to force a deploy from a branch other than the Default without connecting it in your service settings._

## Cancel

Users can cancel deployments in progress by clicking the three dots at the end
of the deployment tab and select Abort deployment. This will cancel the
deployment in progress.

## Remove

If a deployment is completed, you can remove it by clicking the three dots
at the end of the deployment tab and select Remove. This will remove the
deployment and stop any further project usage.

## Restart a crashed deployment

When a Deployment is Crashed, it is no longer running because the underlying process exited with a non-zero exit code - if your deployment exits successfully (exit code 0), the status will remain Success.

Railway automatically restarts crashed Deployments up to 10 times (depending on your Restart Policy). After this limit is reached, your deployment status is changed to Crashed and notifying webhooks & emails are sent to the project's members.

Restart a Crashed Deployment by visiting your project and clicking on the "Restart" button that appears in-line on the Deployment:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1643239507/crash-ui_b2yig1.png"
alt="Screenshot of Deploy Options"
layout="responsive"
width={947} height={156} quality={80} />

Restarting a crashed Deployment restores the exact image containing the code & configuration of the original build. Once the Deployment is back online, its status will change back to Success.

You can also click within a deployment and using the Command Palette restart a deployment at any state.

## Deployment dependencies - startup ordering

You can control the order your services start up with Reference Variables.
When one service references another, it will be deployed after the service it is referencing when applying a staged change or duplicating an environment.

Services that have circular dependencies will simply ignore them and deploy as normal.

For example, let's say you're deploying an API service that depends on a PostgreSQL database.

When you have services with reference variables like:

- API Service has DATABASE_URL=${{Postgres.DATABASE_URL}} which is defined on your Postgres Service in the same project.

Railway will:

1. Deploy the Postgres Service first
2. Then deploy the API Service (since it has a reference variable to Postgres)


# GitHub autodeploys
Source: https://docs.railway.com/deployments/github-autodeploys

Learn how to configure GitHub autodeployments.



## Configure the GitHub branch for deployment triggers

To update the branch that triggers automatic deployments, go to your Service Settings and choose the appropriate trigger branch.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1713907838/docs/triggerBranch_tzf9q3.png"
alt="Screenshot of GitHub Integration"
layout="responsive"
width={903} height={523} quality={80} />

### Disable automatic deployments

To disable automatic deployment, simply hit Disconnect in the Service Settings menu.

_Note: To manually trigger a deployment from the latest commit, use the Command Palette: CMD + K -> "Deploy Latest Commit". This will deploy the latest commit from the **Default** branch in GitHub._

_Currently, there is no way to force a deploy from a branch other than the Default without connecting it in your service settings._

## Wait for CI

<Banner variant="info">
  Please make sure you have{" "}
  <a href="https://github.com/settings/installations" target="_blank">accepted the updated GitHub permissions</a>
  required for this feature to work.
</Banner>

To ensure Railway waits for your GitHub Actions to run successfully before triggering a new deployment, you should enable **Wait for CI**.

#### Requirements

- You must have a GitHub workflow defined in your repository.
- The GitHub workflow must contain a directive to run on push:

### Enabling wait for CI

If your workflow satisfies the requirements above, you will see the Wait for CI flag in service settings.

<Image src="https://res.cloudinary.com/railway/image/upload/v1730324753/docs/deployments/waitforci_dkfsxy.png" alt="Check Suites Configuration" layout="responsive" width={1340} height={392} quality={80} />

Toggle this on to ensure Railway waits for your GitHub Actions to run successfully before triggering a new deployment.

When enabled, deployments will be moved to a WAITING state while your workflows are running.

If any workflow fails, the deployments will be SKIPPED.

When all workflows are successful, deployments will proceed as usual.

## Code Examples

on:
    push:
      branches:
        - main


# Image auto updates
Source: https://docs.railway.com/deployments/image-auto-updates

Learn how to automatically keep your Docker images up to date with scheduled maintenance windows.



## Supported registries

Image auto updates are only available for images hosted on the following registries:

- **Docker Hub** (docker.io or no domain prefix)
- **GitHub Container Registry** (ghcr.io)

Images from other registries (ECR, GCR, ACR, private registries, etc.) do not support auto updates.

## How it works

Railway periodically checks the Docker registry for new versions of your configured image. When an update is available and your maintenance window is active, Railway will:

1. Create a backup of any attached volumes
2. Redeploy your service with the updated image
3. Notify workspace admins of the update

### Update behavior by tag type

How Railway handles updates depends on the type of tag you've configured:

#### Semantic version tags

For tags like :v1.2.3 or :1.0.0, Railway checks for newer versions and updates your service configuration to the new tag (e.g., :v1.2.3 -> :v1.2.4).

You can choose your update preference in the auto updates settings either **patches only** or **minor updates and patches**:

!Update preference setting

When a new version matching your preference is detected, you'll see a notification:

!Patch version available

#### Non-semantic version tags

For tags like :latest, :canary, or :staging, Railway monitors for new image pushes to that specific tag. When a new image is pushed (same tag, different SHA), Railway redeploys your service.

Your configured tag is always preserved. Railway does **not** switch non-semver tags to :latest. If you configure :canary, Railway only redeploys when a new image is pushed to :canary.

## Configure auto updates

To enable automatic image updates:

1. Navigate to your service's **Settings** page
2. Under the **Source** section, select **Configure Auto Updates**
3. Choose your preferred update type
4. Choose a maintenance window

<video src="https://res.cloudinary.com/railway/video/upload/v1767630771/Schedule_jvpido.mp4" controls autoplay loop muted playsinline/>

## Maintenance Windows

Maintenance windows define when Railway is allowed to apply automatic updates. All schedules are evaluated in **UTC**.

| Window | Schedule |
| ------ | -------- |
| **Weekends** | Saturday and Sunday, all day |
| **Night** | 02:00 - 06:00 UTC daily |
| **Anytime** | Updates are applied immediately after detection |
| **Custom** | User-defined day and hour ranges |

Note that updates are applied after Railway detects new versions, not the moment they're published. To avoid overwhelming registries, detection results are cached for up to a few hours.

### Custom schedules

Custom maintenance windows let you define days and hour ranges for updates. You can configure multiple windows to match your operational requirements.

<video src="https://res.cloudinary.com/railway/video/upload/v1767630800/CustomSchedule_xau6q1.mp4" controls autoplay loop muted playsinline />

## Safety features

Railway includes several safety mechanisms to protect your services during automatic updates:

### Volume backups

For Pro plan users, Railway automatically creates a backup of all volumes attached to the service before applying any update. These backups are named Auto Update {image} and can be used to restore data if needed.

### Skip versions

If a specific version causes issues, you can skip it to prevent Railway from automatically updating to that version. Skipped versions will be excluded from future auto-update checks.

When prompted select the dropdown and click "Skip this version" 

!Skip version dialog

## Notifications

When an automatic update is applied, workspace admins receive a notification containing:

- Service and environment name
- Previous version
- New version
- Update type

To disable these notifications, create a custom rule setting "ServiceInstance Auto Updated" to "None" for a project.


# Optimize performance
Source: https://docs.railway.com/deployments/optimize-performance

Explore quick ways to optimize your app's performance on Railway.

Specifically, we offer the following features:

- Horizontal Scaling with Replicas where each individual replica can use the full resources your plan allows for. (Vertical scaling is done automatically)
- Regional Deployments

Continue reading for information on how to configure these.

## Configure horizontal scaling

Scale horizontally by manually increasing the number of replicas for a service.

Each replica has access to the full resources allocated by your plan. For instance, with the Pro plan, each of your replicas can utilize up to 24 vCPU and 24GB of memory, for example, if you had 2 replicas, your service would be able to utilize up to 48 vCPU and 48GB of memory split between the 2 replicas.

Railway's infrastructure spans multiple regions across the globe, and by default Railway deploys to your preferred region.

<Image 
    src="https://res.cloudinary.com/railway/image/upload/v1733386054/multi-region-replicas_zov7rv.png"
    alt="Multi-region replicas"
    layout="responsive"
    width={1370}
    height={934}
/>

To change the number of replicas per deploy within your service, go to the service settings view and look for the "Regions" field in the "Deploy" section. This will create multiple instances of your service and distribute traffic between them.

_Additional regions may be added in the future as Railway continues expanding its infrastructure footprint._

### Replica ID environment variable

Each replica will be deployed with a Railway-provided environment variable named RAILWAY_REPLICA_ID which can be used for logging and monitoring, for example.

### Replica region environment variable

Each replica will be deployed with a Railway-provided environment variable named RAILWAY_REPLICA_REGION which can be used for logging and monitoring, for example.

### Load balancing between replicas

If you are using multi-region replicas, Railway will automatically route public traffic to the nearest region and then randomly distribute requests to the replicas within that region.

If you are using a single region with multiple replicas, Railway will randomly distribute public traffic to the replicas of that region.

**Note:** For now Railway does not support sticky sessions nor report the usage of the individual replicas within the metrics view, all metrics are aggregated across all replicas in all regions.

### Set a preferred region

To set a default or preferred region, do so from your Workspace Settings.

### Impact of region changes

For information on the impact of changing a service's region, see the Regions reference guide.

## Singleton deploys

By default, Railway maintains only one deploy per service.


# Healthchecks
Source: https://docs.railway.com/deployments/healthchecks

Learn how to configure health checks to guarantee zero-downtime deployments of services on Railway.



## How it works

When a new deployment is triggered for a service, if a healthcheck endpoint is configured, Railway will query the endpoint until it receives an HTTP 200 response. Only then will the new deployment be made active and the previous deployment inactive.

**Note:** Railway does not monitor the healthcheck endpoint after the deployment has gone live.

## Configure the healthcheck path

To configure a healthcheck:

1. Ensure your webserver has an endpoint (e.g. /health) that will return an HTTP status code of 200 when the application is live and ready.

2. Under your service settings, input your health endpoint. Railway will wait for this endpoint to serve a 200 status code before switching traffic to your new endpoint.

## Configure the healthcheck port

Railway will inject a PORT environment variable that your application should listen on.

This variable's value is also used when performing health checks on your deployments.

If your application doesn't listen on the PORT variable, possibly due to using target ports, you can manually set a PORT variable to inform Railway of the port to use for health checks.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743469112/healthcheck-port_z0vj4o.png"
alt="Screenshot showing PORT service variable configuration"
layout="intrinsic"
width={1200} height={307} quality={100} />

Not listening on the PORT variable or omitting it when using target ports can result in your health check returning a service unavailable error.

## Healthcheck timeout

The default timeout on healthchecks is 300 seconds (5 minutes). If your application fails to serve a 200 status code during this allotted time, the deploy will be marked as failed.

<Image 
src="https://res.cloudinary.com/railway/image/upload/v1664564544/docs/healthcheck-timeout_lozkiv.png"
alt="Screenshot of Healthchecks Timeouts"
layout="intrinsic"
width={1188} height={348} quality={80} />

To increase the timeout, change the number of seconds on the service settings page, or with a RAILWAY_HEALTHCHECK_TIMEOUT_SEC service variable.

## Services with attached volumes

To prevent data corruption, we prevent multiple deployments from being active and mounted to the same service. This means that there will be a small amount of downtime when re-deploying a service that has a volume attached, even if there is a healthcheck endpoint configured.

## Healthcheck hostname

Railway uses the hostname healthcheck.railway.app when performing healthchecks on your service. This is the domain from which the healthcheck requests will originate.

For applications that restrict incoming traffic based on the hostname, you'll need to add healthcheck.railway.app to your list of allowed hosts. This ensures that your application will accept healthcheck requests from Railway.

If your application does not permit requests from that hostname, you may encounter errors during the healthcheck process, such as "failed with service unavailable" or "failed with status 400".

## Continuous healthchecks

The healthcheck endpoint is currently **_not used for continuous monitoring_** as it is only called at the start of the deployment, to ensure it is healthy prior to routing traffic to it.

If you are looking for a quick way to setup continuous monitoring of your service(s), check out the <a href="https://railway.com/deploy/p6dsil" target="_blank">Uptime Kuma template</a> in the template marketplace.


# Restart policy
Source: https://docs.railway.com/deployments/restart-policy

Learn how to configure the restart policy so that Railway can automatically restart your service if it crashes.

**Note:** For services with multiple replicas, a restart will only affect the replica that crashed, while the other replica(s) continue handling the workload until the restarted replica is back online.

The default is On Failure with a maximum of 10 restarts.

To configure a different restart policy, go to the Service settings and select a different policy from the dropdown.

#### What does each policy mean?

- Always: Railway will automatically restart your service every time it stops, regardless of the reason.

- On Failure: Railway will only restart your service if it stops due to an error (e.g., crashes, exits with a non-zero code).

- Never: Railway will never automatically restart your service, even if it crashes.

#### Plan limitations

Users on the Free plan and those trialing the platform have some limitations on the restart policy:

- Always Is not available.

- On Failure is limited to 10 restarts.

Users on paid plans can set any restart policy with any number of restarts.


# Deployment teardown
Source: https://docs.railway.com/deployments/deployment-teardown

Learn how to configure the deployment lifecycle to create graceful deploys with zero downtime.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1750178677/docs/deployment-teardown-guide/s5pqob0j8nreoojbo6dj.png"
alt="Screenshot of a teardown settings"
layout="responsive"
width={642} height={324} quality={80}/>

To learn more about the full deployment lifecycle, see the deploy reference.

#### Overlap time

Once the new deployment is active, the previous deployment remains active for a configurable amount of time. You can control this via the "Settings" pane for the service. It can also be configured via code or the RAILWAY_DEPLOYMENT_OVERLAP_SECONDS service variable.

#### Draining time

Once the new deployment is active, the previous deployment is sent a SIGTERM signal and given time to gracefully shutdown before being forcefully stopped with a SIGKILL. The time to gracefully shutdown can be controlled via the "Settings" pane. It can also be configured via code or the RAILWAY_DEPLOYMENT_DRAINING_SECONDS service variable.


# Monorepo
Source: https://docs.railway.com/deployments/monorepo

Learn how to deploy monorepos on Railway.

1. **Isolated Monorepo** â A repository that contains components that are completely isolated to the
   directory they are contained in (eg. JS frontend and Python backend)
1. **Shared Monorepo** â A repository that contains components that share code or configuration from the root directory (eg. Yarn workspace or Lerna project). We support **automated import of Javascript monorepos** for pnpm, npm, yarn or bun monorepos.

For a full step by step walk through on deploying an isolated Monorepo see the <a href="/tutorials/deploying-a-monorepo" target="_blank">tutorial</a> on the subject.

## Deploying an isolated monorepo

The simplest form of a monorepo is a repository that contains two completely
isolated projects that do not share any code or configuration.

To deploy this type of monorepo on Railway, define a root directory for the service.

1. Select the service within the project canvas to open up the service view.
2. Click on the Settings tab.
3. Set the root directory option. Setting this means that Railway will only pull down files from that directory when creating new deployments.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1637798659/docs/root-directory_achzga.png"
alt="Screenshot of root directory configuration"
layout="intrinsic"
width={980} height={380} quality={80} />

**Note:** The **Railway Config File** does not follow the **Root Directory** path. You have to specify the absolute path for the railway.json or railway.toml file, for example: /backend/railway.toml

## Deploying a shared monorepo

Popular in the JavaScript ecosystem, shared monorepos contain multiple components that all share a common root directory.

By default, all components are built with a single command from the root directory (e.g. npm run build). You can override the build command in the service settings.

To deploy this type of monorepo in Railway, define a separate custom start
command in Service Settings for each project that references the monorepo
codebase.

1. Select the service within the project canvas to open the service view.
2. Click on the Settings tab.
3. Set the start command, e.g. npm run start:backend and npm run start:frontend

<Image
src="https://res.cloudinary.com/railway/image/upload/v1637798815/docs/custom-start-command_a8vcxs.png"
alt="Screenshot of custom start command configuration"
layout="intrinsic"
width={1302} height={408} quality={80} />

## Automatic import for JavaScript monorepos

When you import a Javascript monorepo via the project creation page, we automatically detect if it's a monorepo and stage a service for each deployable package. This works for pnpm, npm, yarn and bun.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1758927698/docs/guides/monorepos/monorepo-import-new-page_izirrr.png"
alt="Importing a monorepo from /new"
layout="intrinsic"
width={905} height={642} quality={80} />

<Image
src="https://res.cloudinary.com/railway/image/upload/v1758927701/docs/guides/monorepos/monorepo-import-result_jbtccl.png"
alt="Staged monorepo services"
layout="intrinsic"
width={1369} height={714} quality={80} />

For each package detected, Railway automatically configures:

- **Service Name**: generated from the package name or directory
- **Start Command**: workspace-specific commands like pnpm --filter [package] start
- **Build Command**: workspace-specific commands like pnpm --filter [package] build
- **Watch Paths**: set to the package directory (e.g., /packages/backend/**)
- **Config as Code**: railway.json / railway.toml are detected at the root of the package directory

Railway filters out non-deployable packages such as configuration packages (eslint, prettier, tsconfig) and test packages.

## Watch paths

To prevent code changes in one service from triggering a rebuild of other services in your monorepo, you should configure watch paths.

Watch paths are <a href="https://git-scm.com/docs/gitignore#_pattern_format" target="_blank">gitignore-style</a> patterns that can be used to trigger a new deployment based on what file paths have changed.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743192841/docs/watch-paths_zv62py.png"
alt="Screenshot of Railway Watch Paths"
layout="responsive"
width={1200} height={456} quality={80} />

A monorepo might want to only trigger builds if files are changed in the /packages/backend directory, for example.

## Using the CLI

When interacting with your services deployed from a monorepo using the CLI, always ensure you are "linked" to the appropriate service when executing commands.

To link to a specific service from the CLI, use railway link and follow the prompts.

## Code Examples

âââ frontend/
â   âââ index.js
â   âââ ...
âââ backend/
    âââ server.py
    âââ ...

âââ package.json
âââ packages
    âââ backend
    â   âââ index.js
    âââ common
    â   âââ index.js
    âââ frontend
        âââ index.jsx


# Staged changes
Source: https://docs.railway.com/deployments/staged-changes

Discover how to use staged changes in Railway to deploy updates gradually.

It is important to be familiar with this flow as you explore the upcoming guides.

### What to expect

As you create or update components within your project:

1. The number of staged changes will be displayed in a banner on the canvas
2. Staged changes will appear as purple in the UI

<Image src="https://res.cloudinary.com/railway/image/upload/v1743124823/docs/what-to-expect_geldie.png"
            alt="Staged changes on Railway canvas"
            layout="responsive"
            width={1400} height={720} quality={100} />

### Review and deploy changes

To review the staged changes, click the "Details" button in the banner. Here, you will see a diff of old and new values. You can discard a change by clicking the "x" to the right of the change.

You can optionally add a commit message that will appear in the activity feed.

<Image src="https://res.cloudinary.com/railway/image/upload/v1743123181/docs/changes_qn15ls.png"
            alt="Staged changes on Railway canvas"
            layout="responsive"
            width={1200} height={792} quality={100} />

Clicking "Deploy" will deploy all of the changes at once. Any services that are affected will be redeployed.

Holding the "Alt" key while clicking the "Deploy" button allows you to commit the changes without triggering a redeploy.

### Caveats

- Networking changes are not yet staged and are applied immediately
- Adding databases or templates will only affect the current environment. However, they do not yet create a commit in the history


# Serverless
Source: https://docs.railway.com/deployments/serverless

Learn how Serverless reduces cost usage on Railway.

Serverless allows you to increase the efficiency of resource utilization on Railway and may reduce the usage cost of a service, by ensuring it is running only when necessary.

## How it works

When Serverless is enabled for a service, Railway automatically detects inactivity based on outbound traffic.

#### Inactive service detection

Inactivity is based on the detection of any outbound packets, which could include network requests, database connections, or even NTP. If no packets are sent from the service for over 10 minutes, the service is considered inactive.

Some things that can prevent a service from being put to sleep -

- Keeping active database connections open, such as a database connection pooler.
- Frameworks that report telemetry to their respective services, such as Next.js.
- Making requests to other services in the same project over the private network.
- Making requests to other Railway services over the public internet.
- Making requests to external services over the public internet.
- Receiving traffic from other services in the same project over the private network.
- Receiving traffic from other Railway services over the public internet.
- Receiving traffic from external services over the public internet.

It's important to note that the networking graph in the metrics tab only displays public internet traffic. If you're using a private network to communicate with other services, this traffic won't appear in the metrics tab. However, it's still counted as outbound traffic and will prevent the service from being put to sleep.

#### Waking a service up

A service is woken when it receives traffic from the internet or from another service in the same project through the private network.

The first request made to a slept service wakes it. It may take a small amount of time for the service to spin up again on the first request (commonly known as "cold boot time").

## Caveats

- There will be a small delay in the response time of the first request sent to a slept service (commonly known as "cold boot times")
- For Railway to put a service to sleep, a service must not send _outbound_ traffic for at least 10 minutes. Outbound traffic can include telemetry, database connections, NTP, etc. Inbound traffic is excluded from considering when to sleep a service.
- Enabling Serverless will apply the setting across all Replicas
- Slept services still consume a slot on Railway's infrastructure, enabling Serverless de-prioritizes your workload and in remote cases, may require a rebuild to re-live the service.

## Support

For information on how to enable Serverless on your services refer to the how to guide.


# Regions
Source: https://docs.railway.com/deployments/regions

Deploy your apps across multiple Railway regions worldwide.

Consider factors like compliance needs and proximity to your users when choosing a region.

## Region options

Railway has deploy regions in the Americas, Europe, and Asia-Pacific to provide broad coverage around the world.

Within the service settings, you can select one of the following regions:

| Name                 | Location               | Region Identifier        |
| -------------------- | ---------------------- | ------------------------ |
| US West Metal        | California, USA        | us-west2               |
| US East Metal        | Virginia, USA          | us-east4-eqdc4a        |
| EU West Metal        | Amsterdam, Netherlands | europe-west4-drams3a   |
| Southeast Asia Metal | Singapore              | asia-southeast1-eqsg3a |

<Image
    quality={100}
    width={1359}
    height={651}
    src="https://res.cloudinary.com/railway/image/upload/v1695660846/docs/service_region_picker.png"
    alt="Region picker in service settings"
/>

**Notes:**

- Additional regions may be added in the future as Railway continues expanding its infrastructure footprint.

- The region identifier is the value that can be used in your Config as Code file.

- By default, Railway deploys to your preferred region, which you can change in your Account Settings.

- All regions provide the same experience, performance, and reliability you expect from Railway.

## Impact of region changes

The region of a service can be changed at any time, without any changes to your domain, private networking, etc.

There will be no downtime when changing the region of a service, except if it has a volume attached to it (see below).

### Volumes

Volumes follow the region of the service to which they are attached. This means if you attach a new volume to a service, it will be deployed in the same region as the service.

If you change the region of a service with an attached volume, the volume will need to be migrated to the new region.

<Image
    quality={100}
    src="https://res.cloudinary.com/railway/image/upload/v1695660986/docs/volume_migrate_modal.png"
    alt="Volume migration modal"
    width={669}
    height={678}
/>

Note that this migration can take a while depending on the size of the volume, and will cause downtime of your service during that time.

<Image
    quality={100}
    src="https://res.cloudinary.com/railway/image/upload/v1695661106/docs/volume_migration.png"
    alt="Volume migration in progress"
    width={732}
    height={483}
/>

The same is true if you attach a detached volume to a service in a different region. It will need to be migrated to the new region, which can take a while and cause downtime.

## Configuring regions

For information on how to deploy your services to different regions, refer to the optimize performance guide.


# Scaling
Source: https://docs.railway.com/deployments/scaling

Learn how to scale your applications on Railway.



## How it works

### Vertical autoscaling

By default Railway will scale your service up to the specified vCPU and Memory limits of your plan.

### Horizontal scaling with replicas

Scale horizontally by manually increasing the number of replicas for a service in the service settings. Increasing the number of replicas on a service will create multiple instances of the service deployment.

Each replica has access to the full resources allocated by your plan. For instance, with the Pro plan, each of your replicas can utilize up to 24 vCPU and 24GB of memory, for example, if you had 2 replicas, your service would be able to utilize up to 48 vCPU and 48GB of memory split between the 2 replicas.

#### Multi-region replicas

Multi-region replicas are exactly as advertised -- horizontally scaled replicas that are located in different geographic regions.

The service settings panel will reveal an interface for assigning replicas to different regions.

<Image 
    src="https://res.cloudinary.com/railway/image/upload/v1733386054/multi-region-replicas_zov7rv.png"
    alt="Multi-region replicas"
    layout="responsive"
    width={1370}
    height={934}
/>

Creating, deleting, and re-assigning replicas will trigger a staged change. When applied, Railway scales your service without triggering a full redeploy. New replicas start using the existing deployment image, and removed replicas are drained gracefully.

#### Load balancing between replicas

If you are using multi-region replicas, Railway will automatically route public traffic to the nearest region and then randomly distribute requests to the replicas within that region.

If you are using a single region with multiple replicas, Railway will randomly distribute public traffic to the replicas of that region.

#### Metrics

For services with multiple replicas, the metrics from all replicas are summed up and displayed in the metrics tab, for example, if you have 2 replicas, each using 100 MB of memory, the memory usage displayed in the metrics tab will be 200 MB.

#### Sticky sessions

For now Railway does not support sticky sessions nor report the usage of the replicas within the metrics view.

## Support

For information on how to use horizontal scaling with replicas, refer to this guide.


# Reference
Source: https://docs.railway.com/deployments/reference

Deployments are attempts to build and deliver your service. Learn how they work on Railway.

All deployments will appear in the deployments view on your selected service.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1645148376/docs/deployment-photo_q4q8in.png"
alt="Screenshot of Deploy View"
layout="responsive"
width={1103} height={523} quality={80} />

## How it works

Upon service creation, or when changes are detected in the service source, Railway will build the service and package it into a container with Railpack or a Dockerfile if present. If the source is a Docker Image, the build step is skipped.

Railway then starts the service using either the detected or configured Start Command.

This cycle represents a deployment in Railway.

## Deployment states

A comprehensive up to date list of statues can be found in Railway's GraphQL playground under DeploymentStatus (screenshot).

Deployments can be in any of the following states:

#### Initializing

Every Deployment in Railway begins as Initializing - once it has been accepted into Railway's build queue, the status will change to Building.

#### Building

While a Deployment is Building, Railway will attempt to create a deployable Docker image containing your code and configuration (see Builds).

#### Deploying

Once the build succeeds, Railway will attempt to deploy your image and the Deployment's status becomes Deploying. If a healthcheck is configured, Railway will wait for it to succeed before proceeding to the next step.

#### Failed

If an error occurs during the build or deploy process, the Deployment will stop and the status will become Failed.

#### Active

Railway will determine the deployment's active state with the following logic -

- If the deployment **has** a healthcheck configured, Railway will mark the deployment as Active when the healthcheck succeeds.

- If the deployment **does not** have a healthcheck configured, Railway will mark the deployment as Active after starting the container.

#### Completed

This is the status of the Deployment when the running app exits with a zero exit code.

#### Crashed

A Deployment will remain in the Active state unless it crashes, at which point it will become Crashed.

#### Removed

When a new Deployment is triggered, older deploys in a Active, Completed, or a Crashed state are eventually removed - first having their status updated to Removing before they are finally Removed. Deployments may also be removed manually.

The time from when a new deployment becomes Active until the previous deployment is removed can be controlled by setting a RAILWAY_DEPLOYMENT_OVERLAP_SECONDS service variable.

## Deployment menu

The deployment menu contains actions you can take on a deployment.

**Note:** Some actions are only available on certain deployment states.

<Image
  src="https://res.cloudinary.com/railway/image/upload/v1726503037/docs/redeploy_remove_deploy_jescm0.png"
  alt="Deployment Menu"
  width={1007}
  height={690}
  quality={80}
/>

#### View logs

Opens the deployment up to the corresponding logs, during build the build logs will be shown, during deploy the deploy logs will be shown.

#### Restart

Restarts the process within the deployment's container, this is often used to bring a service back online after a crash or if you application has locked up.

#### Redeploy

Redeploys the selected deployment.

This is often used to bring a service back online after -

- A crash.
- A usage limit has been reached and raised.
- Upgrading to Hobby when trial credits were previously depleted.
- Being demoted from Hobby to free and then upgrading again.

**Notes** -

- The redeploy will use the source code from the selected deployment.

- Deployments older than your plan's retention policy cannot be restored via rollback, and thus the rollback option will not be visible.

#### Rollback

Redeploys the selected deployment.

**Notes** -

- The rollback will use the source code from the selected deployment.

- Deployments older than your plan's retention policy cannot be restored via rollback, and thus the rollback option will not be visible.

#### Remove

Stops the currently running deployment, this also marks the deployment as REMOVED and moves it into the history section.

#### Abort

Cancels the selected initializing or building deployment, this also marks the deployment as REMOVED and moves it into the history section.

## Ephemeral storage

Every service deployment has access to 10GB of ephemeral storage. If a service deployment consumes more than 10GB, it can be forcefully stopped and redeployed.

If your service requires data to persist between deployments, or needs more than 10GB of storage, you should add a volume.

## Singleton deploys

By default, Railway maintains only one deploy per service.

In practice, this means that if you trigger a new deploy either manually or automatically, the old version will be stopped and removed with a slight overlap for zero downtime.

Once the new deployment is online, the old deployment is sent a SIGTERM signal. By default, it is given 0 seconds to gracefully shutdown before being forcefully stopped with a SIGKILL. We do not send any other signals under any circumstances.

The time given to gracefully shutdown can be controlled by setting a RAILWAY_DEPLOYMENT_DRAINING_SECONDS service variable.

## Railway initiated deployments

Occasionally, Railway will initiate a new deployment to migrate your service from one host to another. This may happen for one of three reasons:

1. At your plan tier, such as Trial or Hobby, you may be pre-emptively moved to a different host to help us optimize workload distribution.
2. A host requires security or performance updates and requires there to be no running workloads on the machine. We provide advance warning for these events.
3. A host has a fault and we migrate workloads off the machine to another to maintain customer service continutity.

We perform these migrations when implementing security patches or platform upgrades to the underlying infrastructure where your service was previously running. During platform-wide upgrades, your service might be redeployed multiple times as we roll out changes across Railway's infrastructure. These deployments are mandatory and cannot be opted out of.

These Railway-initiated deployments will display with a banner above the Active deployment to clearly identify them.

## Deployments paused - limited access

Railway's core offering is dynamic, allowing you to vertically or horizontally scale with little-to-no-notice. To offer this flexibility to customers, Railway takes the stance that Pro/Enterprise tiers may, in rare occasions, be prioritized above Free/Hobby tiers.

During periods where Pro/Enterprise users require additional resources, Railway may temporarily suspend resource allocation, including builds, to Free, and more rarely Hobby, customers.

<Image
  src="https://res.cloudinary.com/railway/image/upload/v1749837403/CleanShot_2025-06-13_at_10.55.34_2x_ks2adh.png"
  alt="Limited Access indicator shown during high traffic periods"
  layout="responsive"
  width={1200}
  height={479}
  quality={100}
/>

### During a pause

- You'll see a "Limited Access" indicator in your dashboard
- New deployments will be queued rather than immediately processed
- All other Railway features remain fully functional
- No data or existing deployments are affected

### Continue deploying during high traffic

If you need to deploy immediately during a high traffic pause, you can upgrade to the Pro plan to bypass the deployment queue. Pro tier customers are not affected by deployment pausing and can continue deploying normally during high traffic periods.

### When normal operations resume

- Queued deployments will automatically process in order
- You'll receive a notification when deployment capabilities are restored
- No action is required on your part

## Support

For information on how to manage your deployments, explore the guides in this section.


# Slow deployments
Source: https://docs.railway.com/deployments/troubleshooting/slow-deployments

Learn how to diagnose and fix slow deployments and application performance issues on Railway.



## Understanding deployment phases

Every deployment on Railway goes through several distinct phases. Understanding these phases helps you identify where delays are occurring.

### Phase overview

| Phase | What Happens | Typical Duration |
|-------|--------------|------------------|
| **Initialization** | Railway takes a snapshot of your code | Seconds |
| **Build** | Your code is built into a container image | 1-10+ minutes |
| **Pre-Deploy** | Dependencies are checked and volumes are migrated if needed | Seconds to minutes |
| **Deploy** | Container is created and started | 30 seconds to 2 minutes |
| **Network** | Healthchecks run (if configured) | Up to 5 minutes (configurable) |
| **Post-Deploy** | Previous deployment is drained and removed | Seconds |

### Detailed phase breakdown

#### Initialization (snapshot Code)

Railway captures a snapshot of your source code. This is typically fast unless you have an unusually large repository or many files.

#### Build phase

The build phase is often the longest part of a deployment. Railway uses Railpack (or a Dockerfile if present) to build your application into a container image.

Common causes of slow builds:
- Large dependency trees (many npm packages, Python dependencies, etc.)
- No build caching (first build or cache invalidation)
- Compiling native extensions
- Large assets being processed

**Tip:** Check the build logs to see which steps are taking the longest.

#### Pre-deploy

This phase handles:
- **Waiting for dependencies**: If your service depends on another service that's also deploying, Railway waits for it to be ready
- **Volume migration**: If you changed your service's region and it has a volume attached, the volume data must be migrated. This can take significant time depending on volume size

#### Deploy (creating containers)

This phase involves:
1. **Pulling the container image** to the compute node
2. **Creating the container** with your configuration
3. **Mounting volumes** if configured
4. **Starting your application**

Large container images take longer to pull. Railway caches images on compute nodes when possible, but the first deployment to a new node requires a full pull.

#### Network (healthchecks)

If you have a healthcheck configured, Railway queries your healthcheck endpoint until it receives an HTTP 200 response. The default timeout is 300 seconds (5 minutes).

If your application takes time to:
- Initialize database connections
- Load large files into memory
- Warm up caches

...the healthcheck phase will reflect that startup time.

#### Post-deploy (drain instances)

Railway stops and removes the previous deployment. By default, old deployments are given 0 seconds to gracefully shut down (configurable via RAILWAY_DEPLOYMENT_DRAINING_SECONDS).

## Is it Railway or my app?

Before diving into optimization, determine whether the slowness is on Railway's side or within your application. In the vast majority of cases, performance issues originate from the application itself, rather than the platform. This could be from inefficient queries, resource constraints, or configuration problems.

### Check Railway status

Visit status.railway.com to see if there are any ongoing incidents or degraded performance affecting the platform. If there's a platform-wide issue, it will be reported here. If status shows all systems operational, the issue is almost certainly within your application or its dependencies.

### Check build logs

Build logs show output from the build phase (installing dependencies, compiling code, creating the container image). The deployment view shows each phase with timing information.

Look for:
- Dependency installation steps that take disproportionately long
- Cache misses causing full rebuilds
- Large assets being processed

### Check deployment logs

Deployment logs show your application's stdout/stderr while it's running. These help diagnose runtime issues that occur after your app starts.

Look for:
- Database connection errors or timeouts
- Slow query warnings
- Application exceptions or errors
- Healthcheck failures

### Check your application metrics

Railway provides metrics for CPU, memory, and network usage. High resource usage can indicate:
- Your application is resource-constrained
- Inefficient code paths
- Memory leaks causing garbage collection pressure

For deeper insights, consider integrating an Application Performance Monitoring (APM) tool like Datadog, New Relic, or open-source alternatives like OpenTelemetry. APM tools provide distributed tracing, helping you identify slow database queries, external API calls, and bottlenecks that Railway's built-in metrics don't capture.

### Analyze HTTP logs

Railway captures detailed HTTP request logs for every request to your service. These logs are invaluable for identifying slow endpoints and understanding request patterns. For complete documentation on log features and filtering syntax, see the Logs guide.

**Key fields for performance troubleshooting:**

| Field | Description |
|-------|-------------|
| totalDuration | Total time from request received to response sent (ms) |
| upstreamRqDuration | Time your application took to respond (ms) |
| httpStatus | Response status code |
| path | Request path to identify which endpoints are slow |
| responseDetails | Error details if the request failed |
| txBytes / rxBytes | Response and request sizes |

**Finding slow requests:**

Use the log filter syntax to find requests exceeding a duration threshold:

This finds all requests taking longer than 1 second. You can combine filters to narrow down:

**Understanding the timing fields:**

- **totalDuration** includes everything: network time to/from the edge, time in the proxy, and your application's response time
- **upstreamRqDuration** is specifically how long your application took to respond

If totalDuration is high but upstreamRqDuration is low, the latency is in the network path (edge routing, DNS). If upstreamRqDuration is high, the slowness is in your application.

**Identifying error patterns:**

Filter by status code to find failing requests:

Check responseDetails for specific error information, and upstreamErrors for details about connection failures to your application.

### Test locally

If your app is slow on Railway but fast locally, consider:
- Are you hitting external services with higher latency?
- Are you using the correct region for your database?
- Is your application configured to use private networking?

## Common causes of slow applications

### Database queries

Slow database queries are one of the most common causes of application latency.

**Symptoms:**
- API endpoints that worked fast are now slow
- Timeouts on specific operations
- High CPU on your database service

**Solutions:**
- Add database indexes for frequently queried columns
- Use connection pooling
- Review slow query logs
- Consider read replicas for read-heavy workloads

### Wrong region configuration

If your application is in one region but your database is in another, every query incurs geographic latency as traffic travels between regions on Railway's network.

**Symptoms:**
- Consistently high latency on all database operations (typically 50-150ms+ per query depending on distance)

**Solutions:**
- Deploy your application in the same region as your database

### Not using private networking

If services within the same project communicate over the public internet instead of private networking, you add unnecessary latency and incur egress costs. Private networking is for **server-to-server communication only**. It won't work for requests originating from a user's browser.

**Symptoms:**
- Using public URLs (e.g., your-app.up.railway.app) for inter-service communication
- Connection strings using public hostnames
- Unexpectedly high network egress charges on your bill

**Solutions:**
- Use *.railway.internal hostnames for service-to-service communication
- Update connection strings to use private networking addresses and ports
- For frontend applications that need to call backend APIs, use private networking from your server-side code (API routes, SSR) while keeping public URLs for client-side browser requests

**Example:**


### Resource constraints

Your application may be hitting resource limits, causing throttling or OOM (out of memory) kills.

**Symptoms:**
- Application crashes with exit code 137 (OOM killed)
- Consistently high CPU usage at 100%
- Slow response times during high load

**Solutions:**
- Check your metrics to see actual resource usage
- Adjust resource limits if you're consistently hitting them
- Optimize your application's memory and CPU usage
- Consider horizontal scaling for stateless workloads

### Large container images

Large images take longer to pull, especially on first deployment to a new compute node.

**Symptoms:**
- "Creating containers" phase takes several minutes
- Large build output size shown in build logs

**Solutions:**
- Use multi-stage Docker builds to reduce final image size
- Use smaller base images (e.g., Alpine variants)
- Exclude unnecessary files with .dockerignore
- Remove development dependencies from production builds

### Slow application startup

If your application takes time to initialize, it affects the healthcheck phase duration.

**Symptoms:**
- Healthcheck takes a long time to pass
- Application logs show initialization steps running

**Solutions:**
- Defer non-critical initialization to after the app is ready to serve traffic
- Use lazy loading for heavy dependencies
- Increase healthcheck timeout if startup time is legitimate
- Consider a dedicated healthcheck endpoint that responds before full initialization

## What plan upgrades actually do

Upgrading your plan increases your **resource limits**, not guaranteed performance. Understanding this distinction is important.

### What upgrading provides

| Plan | Per-Replica vCPU Limit | Per-Replica Memory Limit |
|------|------------------------|--------------------------|
| **Hobby** | 8 vCPU | 8 GB |
| **Pro** | 24 vCPU | 24 GB |
| **Enterprise** | Custom | Custom |

Upgrading raises the ceiling on how many resources a single replica can use. Your application only uses what it needs, up to the limit.

### When upgrading helps

Upgrading helps when:
- Your metrics show you're hitting current resource limits
- Your application needs more memory (e.g., processing large datasets)
- You need more CPU for compute-intensive tasks
- You want to run more replicas (higher replica limits on higher plans)

### When upgrading doesn't help

Upgrading won't help when:
- Slowness is caused by external services (databases, APIs)
- Your application has inefficient code
- Network latency is the bottleneck
- You're not actually using your current resource allocation

**Always check your metrics before upgrading.** If your service uses 500MB of memory and 0.5 vCPU, upgrading from Hobby to Pro won't make it faster.

## Edge routing and latency

Railway operates edge proxies in multiple regions. For a complete overview of edge infrastructure, see the Edge Networking reference. Understanding how traffic is routed helps diagnose latency issues.

### How edge routing works

When a request comes in:
1. It hits the nearest Railway edge proxy
2. The edge proxy routes it to your service in the configured region
3. Your service processes the request and responds

You can see which edge handled a request via the X-Railway-Edge response header.

### Checking the edge header

The header value shows the region, e.g., railway/us-west2.

### Why traffic might hit the wrong edge

- DNS caching: Your local DNS resolver may have cached an old record
- CDN/Proxy interference: Services like Cloudflare route based on their own logic
- Geographic routing: Users in certain regions may be routed suboptimally

### Optimizing for global users

If you have users worldwide, you can use multi-region replicas to deploy stateless services closer to your users. Railway automatically routes traffic to the nearest region.

**Note:** Multi-region works well for stateless application servers, but databases typically run in a single region. If your app is deployed globally but your database is in one region, replicas far from the database will still experience latency on database queries. To mitigate this:
- Use application-level caching to reduce database round-trips
- Consider database read replicas in additional regions for read-heavy workloads
- Accept the latency trade-off for writes, which must go to the primary database

### Private networking and edge

Private networking (*.railway.internal) bypasses the edge entirely. Services communicate directly within Railway's infrastructure, which is faster than going through the public internet.

## When to contact support

Contact Railway support through Central Station if:

- Deployments are consistently slow with no apparent cause
- You see **544 Railway Proxy Error** responses, which indicate a platform-side issue (as opposed to 502 errors, which indicate application issues)
- The status page shows no issues but you're experiencing degraded performance
- You need help optimizing your deployment configuration

**Tip:** When reporting issues, include the X-Railway-Request-Id header from affected requests. This unique identifier helps Railway support trace your request through the infrastructure. You can find it in your HTTP response headers.

## Code Examples

@totalDuration:>1000

@totalDuration:>500 @path:/api/users @method:GET

@httpStatus:>=500

// Server-side code (API routes, SSR): use private networking
const apiUrl = "http://api.railway.internal:3000";

// Client-side code (browser): must use public URL
const apiUrl = "https://api.up.railway.app";

curl -I https://your-app.up.railway.app | grep -i X-Railway-Edge


# NodeJS SIGTERM handling
Source: https://docs.railway.com/deployments/troubleshooting/nodejs-sigterm-handling

SIGTERM might sometimes fail to process on shutdown. Here's why.

When you start your app with NPM, Yarn, or PNPM, the package manager becomes the main process, not your app.
Because the signal has been intercepted, the service will eventually be force quit which is displayed as a sudden "crash".

The fix is simple: start Node directly.

Head to your service's Settings tab. From there scroll to the "Deploy" section and change "Custom Start Command".

Instead of this:


Use this:


With this change, your app will receive SIGTERM directly and can handle shutdown cleanly.

## Code Examples

npm run start

node index.js


# No start command could be found
Source: https://docs.railway.com/deployments/troubleshooting/no-start-command-could-be-found

Learn how to troubleshoot and fix the 'No Start Command Could be Found' error.

Railway uses Railpack to analyze your application's files to generate a container image for your application.

Seeing the No start command could be found error means that Railway was unable to automatically find an appropriate start command for your application.

A start command is a command that will be executed by Railway to run your application.

## Why this error can occur

By default, Railway uses Railpack to build and run your application. Railpack will try its best to find an appropriate start command for your application.

Some limited examples of start commands that Railway will try are -

For Node based apps it will try to use npm start, yarn start, pnpm start, or bun start if a start script is present in your package.json file.

For Python apps it will try to use python main.py if a main.py file is present, or python manage.py migrate && gunicorn {app_name}.wsgi if a Django application is detected.

For Ruby apps it will try to use bundle exec rails server -b 0.0.0.0 if a Rails application is detected.

Failing the automatic detection, Railway will return the No start command could be found error.

## Possible solutions

Since Railway was unable to find a start command, you will need to specify a start command yourself.

You can do this in the service settings under the Start Command field.

Some common start commands for various frameworks and languages are -

#### Node.js

Where main.js is the entry point for your application, could be index.js, server.js, app.js, etc.

#### Next.js

_Note: The --port flag is needed to ensure that Next.js listens on the correct port._

#### Nuxt.js

This will run Nuxt.js in production mode using its built-in Nitro server.

#### FastAPI

Where main is the name of the file that contains the app variable from FastAPI.

_Note: The --host and --port flags are needed to ensure that FastAPI listens on the correct host and port._

#### Flask

Where main is the name of the file that contains the app variable from Flask.

#### Django

Where myproject is the name of the folder that contains your wsgi.py file.

#### Ruby on Rails

_Note: The -b and -p flags are needed to ensure that Rails listens on the correct host and port._

#### Vite

_Note: The serve command is needed to serve the static site files and can be installed by running npm install serve locally._

#### Create React app

_Note: The serve command is needed to serve the static site files and can be installed by running npm install serve locally._

## Code Examples

node main.js

npx next start --port $PORT

node .output/server/index.mjs

uvicorn main:app --host 0.0.0.0 --port $PORT

gunicorn main:app

gunicorn myproject.wsgi

bundle exec rails server -b 0.0.0.0 -p $PORT

serve --single --listen $PORT dist

serve --single --listen $PORT build



# Data & storage
Source: https://docs.railway.com/data & storage

# Build a database service
Source: https://docs.railway.com/databases/build-a-database-service

Learn how to build a database service on Railway.

For the purpose of this guide, you'll use the official <a href="https://hub.docker.com/_/postgres" target="_blank">Postgres image</a> as an example.

## Service source

As discussed in the Services guide, a crucial step in creating a service is defining a source from which to deploy.

To deploy the official Postgres image, we'll simply enter postgres into the Source Image field:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1701464166/docs/databases/CleanShot_2023-12-01_at_14.54.35_2x_aa5gwt.png"
alt="Screenshot of a Docker image source"
layout="responsive"
width={559} height={168} quality={80} />

## Volumes

Attach a volume to any service, to keep your data safe between deployments. For the Postgres image, the default mount path is /var/lib/postgresql/data.

Just attach a volume to the service you created, at the mount path:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1701464411/docs/databases/mountpath_lajfam.png"
alt="Screenshot of a mount path"
layout="responsive"
width={519} height={168} quality={80} />

## Environment variables

Now, all you need to do is configure the appropriate <a href="https://hub.docker.com/_/postgres#environment-variables:~:text=have%20found%20useful.-,Environment%20Variables,-The%20PostgreSQL%20image" target="_blank">environment variables</a> to let the Postgres image know how to run:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1701464670/docs/databases/envvars_aow79p.png"
alt="Screenshot of environment variables"
layout="responsive"
width={460} height={458} quality={80} />

Note the DATABASE_URL is configured with TCP Proxy variables, but you can also connect to the database service over the private network. More information below.

## Connecting

### Private network

To connect to your database service from other services in your project, you can use the private network. For a postgres database service listening on port 5432, you can use a connection string like this -

### TCP proxy

If you'd like to expose the database over the public network, you'll need to set up a TCP Proxy, to proxy public traffic to the Postgres port 5432:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743194081/docs/tcp-proxy_edctub.png"
alt="Screenshot of TCP proxy configuration"
layout="responsive"
width={1200} height={822} quality={100} />

## Conclusion

That's all it takes to spin up a Postgres service in Railway directly from the official Postgres image. Hopefully this gives you enough direction to feel comfortable exploring other database images to deploy.

Remember you can also deploy from a Dockerfile which would generally involve the same features and steps. For an example of a Dockerfile that builds a custom image with the official Postgres image as base, take a look at <a href="https://github.com/railwayapp-templates/postgres-ssl" target="_blank">Railway's SSL-enabled Postgres image repo</a>.

### Template marketplace

Need inspiration or looking for a specific database? The <a href="https://railway.com/templates" target="_blank">Template Marketplace</a> already includes solutions for many different database services. You might even find a template for the database you need!

Here are some suggestions to check out -

- <a href="https://railway.com/deploy/SMKOEA" target="_blank">Minio</a>
- <a href="https://railway.com/deploy/clickhouse" target="_blank">ClickHouse</a>
- <a href="https://railway.com/deploy/dragonfly" target="_blank">Dragonfly</a>
- <a href="https://railway.com/deploy/kbvIRV" target="_blank">Chroma</a>
- <a href="https://railway.com/deploy/elasticsearch" target="_blank">Elastic Search</a>

## Code Examples

postgresql://postgres:password@postgres.railway.internal:5432/railway


# PostgreSQL
Source: https://docs.railway.com/databases/postgresql

Learn how to deploy a PostgreSQL database on Railway.



## Deploy

Add a PostgreSQL database to your project via the ctrl / cmd + k menu or by clicking the + New button on the Project Canvas.

<Image src="https://res.cloudinary.com/railway/image/upload/v1695934218/docs/databases/addDB_qxyctn.gif"
alt="GIF of the Adding Database"
layout="responsive"
width={450} height={396} quality={100} />

You can also deploy it via the template from the template marketplace.

#### Deployed service

Upon deployment, you will have a PostgreSQL service running in your project, deployed from Railway's SSL-enabled Postgres image, which uses the official Postgres image from Docker Hub as its base.

### Connect

Connect to the PostgreSQL server from another service in your project by referencing the environment variables made available in the PostgreSQL service:

- PGHOST
- PGPORT
- PGUSER
- PGPASSWORD
- PGDATABASE
- DATABASE_URL

_Note, Many libraries will automatically look for the DATABASE_URL variable and use
it to connect to PostgreSQL but you can use these variables in whatever way works for you._

#### Connecting externally

It is possible to connect to PostgreSQL externally (from outside of the project in which it is deployed), by using the TCP Proxy which is enabled by default.

_Keep in mind that you will be billed for Network Egress when using the TCP Proxy._

### Modify the deployment

Since the deployed container is based on an image built from the official PostgreSQL image in Docker hub, you can modify the deployment based on the instructions in Docker hub.

We also encourage you to fork the Railway postgres-ssl repository to customize it to your needs, or feel free to open a PR in the repo!

## Backups and observability

Especially for production environments, performing regular backups and monitoring the health of your database is essential. Consider adding:

- **Backups**: Automate regular backups to ensure data recovery in case of failure. We suggest checking out the native Backups feature.

- **Observability**: Implement monitoring for insights into performance and health of your databases. If you're not already running an observability stack, check out these templates to help you get started building one:
  - Prometheus
  - Grafana
  - PostgreSQL Exporter

## Extensions

In an effort to maintain simplicity in the default templates, we do not plan to add extensions to the PostgreSQL templates covered in this guide.

For some of the most popular extensions, like PostGIS and Timescale, there are several options in the template marketplace.

- <a href="https://railway.com/deploy/VSbF5V" target="_blank">TimescaleDB</a>
- <a href="https://railway.com/deploy/postgis" target="_blank">PostGIS</a>
- <a href="https://railway.com/deploy/timescaledb-postgis" target="_blank">TimescaleDB + PostGIS</a>
- <a href="https://railway.com/deploy/3jJFCA" target="_blank">pgvector</a>

## Modifying the Postgres configuration

You can modify the Postgres configuration by using the ALTER SYSTEM command.

After running the SQL, you will need to restart the deployment for the changes to take effect.

You can restart the deployment by clicking the Restart button in the deployment's 3-dot menu.

## Increasing the SHM size

The SHM Size is the maximum amount of shared memory available to the container.

By default it is set to 64MB.

You would need to change the SHM Size if you are experiencing the following error -

You can modify the SHM Size by setting the RAILWAY_SHM_SIZE_BYTES variable in your service variables.

This variable is a number in bytes, so you would need to convert the size you want to use.

For example, to increase the SHM Size to 500MB, you would set the variable to 524288000.

## Additional resources

While these templates are available for your convenience, they are considered unmanaged, meaning you have total control over their configuration and maintenance.

We _strongly encourage you_ to refer to the source documentation to gain deeper understanding of their functionality and how to use them effectively. Here are some links to help you get started:

- PostgreSQL Documentation
- PostgreSQL High Availability Documentation
- Repmgr Documentation
- Pgpool-II Documentation

## Code Examples

ALTER SYSTEM SET shared_buffers = '2GB';
ALTER SYSTEM SET effective_cache_size = '6GB';
ALTER SYSTEM SET maintenance_work_mem = '512MB';
ALTER SYSTEM SET work_mem = '32MB';
ALTER SYSTEM SET max_worker_processes = '8';
ALTER SYSTEM SET max_parallel_workers_per_gather = '4';
ALTER SYSTEM SET max_parallel_workers = '8';

-- Reload the configuration to save the changes
SELECT pg_reload_conf();

ERROR: could not resize shared memory segment "PostgreSQL.1590182853" to 182853 bytes: no space left on device


# MySQL
Source: https://docs.railway.com/databases/mysql

Learn how to deploy a MySQL database on Railway.

### Deploy

Add a MySQL database to your project via the ctrl / cmd + k menu or by clicking the + New button on the Project Canvas.

<Image src="https://res.cloudinary.com/railway/image/upload/v1695934218/docs/databases/addDB_qxyctn.gif"
alt="GIF of the Adding Database"
layout="responsive"
width={450} height={396} quality={100} />

You can also deploy it via the template from the template marketplace.

#### Deployed service

Upon deployment, you will have a MySQL service running in your project, deployed directly from the mysql Docker image.

### Connect

Connect to MySQL from another service in your project by referencing the environment variables made available in the MySQL service:

- MYSQLHOST
- MYSQLPORT
- MYSQLUSER
- MYSQLPASSWORD
- MYSQLDATABASE
- MYSQL_URL

#### Connecting externally

It is possible to connect to MySQL externally (from outside of the project in which it is deployed), by using the TCP Proxy which is enabled by default.

_Keep in mind that you will be billed for Network Egress when using the TCP Proxy._

### Modify the deployment

Since the deployed container is pulled from the official MySQL image in Docker hub, you can modify the deployment based on the instructions in Docker hub.

## Backups and observability

Especially for production environments, performing regular backups and monitoring the health of your database is essential. Consider adding:

- **Backups**: Automate regular backups to ensure data recovery in case of failure. We suggest checking out the native Backups feature.

- **Observability**: Implement monitoring for insights into performance and health of your databases. If you're not already running an observability stack, check out these templates to help you get started building one:
  - Prometheus
  - Grafana

## Additional resources

While these templates are available for your convenience, they are considered unmanaged, meaning you have total control over their configuration and maintenance.

We _strongly encourage you_ to refer to the source documentation to gain deeper understanding of their functionality and how to use them effectively. Here are some links to help you get started:

- MySQL Documentation
- MySQL InnoDB Cluster Documentation
- MySQL Router Documentation


# Redis
Source: https://docs.railway.com/databases/redis

Learn how to deploy a Redis database on Railway.



## Deploy

Add a Redis database to your project via the ctrl / cmd + k menu or by clicking the + New button on the Project Canvas.

<Image src="https://res.cloudinary.com/railway/image/upload/v1695934218/docs/databases/addDB_qxyctn.gif"
alt="GIF of the Adding Database"
layout="responsive"
width={450} height={396} quality={100} />

You can also deploy it via the template from the template marketplace.

#### Deployed service

Upon deployment, you will have a Redis service running in your project, deployed from the redis Docker image.

### Connect

Connect to the Redis server from another service in your project by referencing the environment variables made available in the Redis service:

- REDISHOST
- REDISUSER
- REDISPORT
- REDISPASSWORD
- REDIS_URL

#### Connecting externally

It is possible to connect to Redis externally (from outside of the project in which it is deployed), by using the TCP Proxy which is enabled by default.

_Keep in mind that you will be billed for Network Egress when using the TCP Proxy._

### Modify the deployment

Since the deployed container is pulled from the redis image in Docker Hub, you can modify the deployment based on the instructions in Docker Hub.

## Backup and monitoring

Especially for production environments, performing backups and monitoring the health of your data is essential. Consider adding:

- **Backups**: Automate regular backups to ensure data recovery in case of failure. We suggest checking out the native Backups feature.

- **Observability**: Implement monitoring for insights into performance and health of your Redis cluster. You can integrate a Redis exporter for Prometheus, although we do not provide a specific template at this time.

## Additional resources

While these templates are available for your convenience, they are considered unmanaged, meaning you have total control over their configuration and maintenance.

We _strongly encourage you_ to refer to the source documentation to gain deeper understanding of their functionality and how to use them effectively. Here are some links to help you get started:

- Redis Documentation
- Redis Replication
- High Availability with Redis Sentinel
- Understanding Sentinels


# MongoDB
Source: https://docs.railway.com/databases/mongodb

Learn how to deploy a MongoDB database on Railway.



## Deploy

Add a MongoDB database to your project via the ctrl / cmd + k menu or by clicking the + New button on the Project Canvas.

<Image src="https://res.cloudinary.com/railway/image/upload/v1695934218/docs/databases/addDB_qxyctn.gif"
alt="GIF of the Adding Database"
layout="responsive"
width={450} height={396} quality={100} />

You can also deploy it via the template from the template marketplace.

#### Deployed service

Upon deployment, you will have a MongoDB service running in your project, deployed from the official mongo Docker image.

#### Custom start command

The MongoDB database service starts with the following Start Command to enable communication over Private Network: mongod --ipv6 --bind_ip ::,0.0.0.0  --setParameter diagnosticDataCollectionEnabled=false

## Connect

Connect to MongoDB from another service in your project by referencing the environment variables made available in the Mongo service:

- MONGOHOST
- MONGOPORT
- MONGOUSER
- MONGOPASSWORD
- MONGO_URL

#### Connecting externally

It is possible to connect to MongoDB externally (from outside of the project in which it is deployed), by using the TCP Proxy which is enabled by default.

_Keep in mind that you will be billed for Network Egress when using the TCP Proxy._

### Modify the deployment

Since the deployed container is pulled from the official MongoDB image in Docker Hub, you can modify the deployment based on the instructions in Docker Hub.

## Backup and monitoring

Especially for production environments, performing regular backups and monitoring the health of your database is essential. Consider adding:

- **Backups**: Automate regular backups to ensure data recovery in case of failure. We suggest checking out the native Backups feature.

- **Observability**: Implement monitoring for insights into performance and health of your database.

## Additional resources

While these templates are available for your convenience, they are considered unmanaged, meaning you have total control over their configuration and maintenance.

We _strongly encourage you_ to refer to the source documentation to gain deeper understanding of their functionality and how to use them effectively. Here are some links to help you get started:

- Mongo Documentation
- Replication in Mongo


# Database view
Source: https://docs.railway.com/databases/database-view

Learn how to read, insert and edit data via the database view on Railway.



## SQL interfaces

<Image src="https://res.cloudinary.com/railway/image/upload/v1701904581/docs/databases/dataTab_vtj7me.png"
alt="Screenshot of Postgres Service Panel"
layout="intrinsic"
width={995} height={528} quality={80} />

For MySQL and Postgres, Railway displays the tables contained within an instance by default; this is called the Table View.

Shift-clicking on one or multiple tables exposes additional options such as the ability to delete the table(s).

### Creating a table

<Image src="https://res.cloudinary.com/railway/image/upload/v1636426105/docs/table_create_kuvnjg.png"
alt="Screenshot of Create Table interface"
layout="intrinsic"
width={928} height={396} quality={80} />

Under the Table View, clicking the Create Table button at the bottom right of the interface navigates users to the Create Table interface.

For each column a user wants to add to the database, the interface accepts a name, type, default_value and constraints. Depending on the SQL database that is used, valid types and constraints may vary.

### Viewing and editing entries

When a table is clicked, the interface navigates into the Entries View.

Under the Entries View, selecting an existing entry exposes the ability to edit the entry. When button that allows one to add entries to the table.

<Image src="https://res.cloudinary.com/railway/image/upload/v1636426105/docs/edit_row_tobmdh.png"
alt="Screenshot of Expanded Project Usage Pane"
layout="intrinsic"
width={803} height={457} quality={80} />

### Add SQL column

Selecting the add column in the entries view opens a modal that prompts you to add a new column to the table.

## Nosql interfaces

For non-structured data, Railway has interfaces that permit users to add and edit data within the service.

### Redis view

<Image src="https://res.cloudinary.com/railway/image/upload/v1636426105/docs/redis_view_jna8ho.png"
alt="Screenshot of Expanded Project Usage Pane"
layout="intrinsic"
width={732} height={419} quality={80} />

With Redis, Railway displays the keys contained within a database instance by default.

### MongoDB document view

With MongoDB, Railway displays a list of document collections. Users can add additional collections or add/edit documents within the collection.

### Adding MongoDB databases

<Image src="https://res.cloudinary.com/railway/image/upload/v1636424673/docs/add_mongo_db_ujjcgr.png"
alt="Screenshot of Expanded Project Usage Pane"
layout="intrinsic"
width={552} height={516} quality={80} />

Within the Collections View, clicking the plus icon next to the top dropdown allows you to create a new Database.

## Credentials tab

The Credentials tab allows you to safely regenerate your database password while keeping the database and environment variables synchronized, avoiding manual variable edits that can cause authentication mismatches.

It's important to manually redeploy any service that depends on the updated password variable (or the derived database URL).

<Image src="https://res.cloudinary.com/railway/image/upload/t_crop/v1756840714/Database_Credentials_ctbwqb.png"
alt="Screenshot of Credentials Data UI Tab"
layout="intrinsic"
width={542} height={422} quality={80} />

## Extensions tab for Postgres

The Extensions tab enables postgres extensions management. You can view, install and uninstall extensions that are available in the official Railway Postgres image.

Extensions that aren't available need to be deployed from templates, since they require additional features in the database's image, like pgvector.

<Image src="https://res.cloudinary.com/railway/image/upload/t_crop/v1756840713/Database_Extensions_flszw9.png"
alt="Screenshot of Extensions Data UI Tab"
layout="intrinsic"
width={540} height={422} quality={80} />


# Reference
Source: https://docs.railway.com/databases/reference

Database services on Railway.

Databases can be deployed into a Railway project from a template, or by creating one through the service creation flow.

## How database services work in Railway

Below are the core concepts to understand when working with databases in Railway.

#### Services

Railway services are containers deployed from a Docker Image or code repository, usually with environment variables defined within the service configuration to control the behavior of the service.

#### Volumes

When deploying a database service, data can be persisted between rebuilds of the container by attaching a Volume to the service.

#### TCP proxy

To access a database service from outside the private network of a particular project, proxy traffic to the exposed TCP port by enabling TCP Proxy on the service.

## Database templates

Many database templates are available to Railway users, which ease the process of deploying a database service.

### Railway-provided templates

Railway provides several templates to provision some of the most popular databases out there. They also deploy with a helpful Database View.

Explore the guides in the How To section for information on how to use these templates -

- PostgreSQL
- MySQL
- MongoDB
- Redis

### Template marketplace

The <a href="https://railway.com/templates" target="_blank">Template Marketplace</a> includes many solutions for database services.

Here are some examples -

- Minio
- ClickHouse
- Dragonfly
- Chroma

## Support

Explore the Databases guide section for more information on how to get started using databases in Railway.


# Backups
Source: https://docs.railway.com/volumes/backups

Learn how Railway handles backups for volume contents to ensure data safety and recovery.



## How it works

When a volume is mounted to a service, backups can be manually created, deleted and restored. And they can also be scheduled to run on a Daily / Weekly / Monthly schedule.

## Backup schedules

Backups can be scheduled to run on a daily, weekly or monthly basis. They will be kept for a number of days / months based on the schedule.

You can set the schedule in the service settings panel, under the Backups tab.

- **Daily** - Backed up every 24 hours, kept for 6 days
- **Weekly** - Backed up every 7 days, kept for 1 month
- **Monthly** - Backed up every 30 days, kept for 3 months

You can select multiple backup schedules for a single volume. These schedules can be modified at any time, and you can also manually trigger backups as needed.

## How to restore a backup

The available backups for a volume are listed in the attached service's Backups tab.

<Image src="https://res.cloudinary.com/railway/image/upload/v1737785142/docs/the-basics/backups_fdx09o.png"
alt="Screenshot of the service backups tab"
layout="responsive"
width={1365} height={765} quality={100} />

To restore a backup, first locate the backup you want to restore via its date stamp, then click the Restore button on the backup.

**Note:** Depending on the size of the backup, this may take a few seconds to a few minutes to complete.

Once completed, we will stage the change for you to review, click the Details button at the top of the project canvas to view the changes.

During this process, you will see a new volume mounted to the same location as the original volume, its name will be the date stamp of the backup.

The previous volume will be retained but has been unmounted from the service, it will have the original volume name such as silk-volume.

**Note:** Restoring a backup will remove any newer backups you may have created after the backup you are restoring, you will still have access to backups older than the one you are restoring.

If everything looks good and you're ready to proceed, click the Deploy button to complete the restore.

The changes will be applied and your service will be redeployed.

## Pricing

Backups are incremental and Copy-on-Write, we only charge for the data exclusive to them, that aren't from other snapshots or the volume itself.

You are only billed for the incremental size of the backup at a rate per GB / minutely, and invoiced monthly. Backups follow the same pricing as Volumes. You can find specific per-minute pricing here.

## Volume backup limits

Volume backups have size limitations based on the volume capacity:

- **Manual backups** are limited to 50% of the volume's total size
- This limitation applies to prevent backup operations from consuming excessive storage resources
- If your data exceeds this threshold, consider growing your volume capacity before creating backups or reaching out to support to raise the limit

## Caveats

Backups are a newer feature that is still under development. Here are some limitations of which we are currently aware:

- Backup incremental sizes are cached for a couple of hours when listed in the frontend, so they may show slightly stale data.
- Wiping a volume deletes all backups.
- Backups can only be restored into the same project + environment.


# Reference
Source: https://docs.railway.com/volumes/reference

Volumes are a feature that enables persistent data for services on Railway.



## How it works

When mounting a volume to a service, a volume is made available to the service on the specified mount path.

## Size limits

Volumes have a default size based on the subscription plan.

- Free and Trial plans: **0.5GB**
- Hobby plans: **5GB**
- Pro plan: **50GB**

Volumes can be "Live resized" after upgrading to a different plan.

Pro users and above can self-serve to increase their volume up to 250 GB.

For Pro and above users, please reach out to us on Central Station if you need more than 250GB. Enterprise users with $2,000/month committed spend can also use Slack.

## Volume limits per project

Each project has a maximum number of volumes that can be created, based on your subscription plan:

| Plan | Maximum Volumes per Project |
|------|----------------------------|
| **Free** | **1** |
| **Trial** | **3** |
| **Hobby** | **10** |
| **Pro** | **20** |

Volumes created for the same service in another environment do not count towards this limit.

Pro users with substantial usage requirements may be eligible for increased volume limits. Please reach out to us on the Railway Help Station to discuss your project's needs.

## I/O specifications

Volumes have the following I/O characteristics:

- **Read IOPS**: 3,000 operations per second
- **Write IOPS**: 3,000 operations per second

These specifications apply to all volume sizes and subscription plans.

## Pricing

Volumes are billed at a rate per GB / minutely, and invoiced monthly. You can find specific per-minute pricing here.

You are only charged for the amount of storage used by your volumes. _Each volume requires approx 2-3% of the total storage to store metadata about the filesystem, so a new volume will always start with some used amount of space used depending on the size._

## Backups

Services with volumes support manual and automated backups, backups are covered in the backups reference guide.

## Deletion and Restoration

When a volume is deleted, it is queued for deletion and will be permanently deleted within 48 hours. You can restore the volume during this period using the restoration link sent via email.

After 48 hours, deletion becomes permanent and the volume cannot be restored.

## Caveats

Here are some limitations of which we are currently aware:

- Each service can only have a single volume
- Replicas cannot be used with volumes
- There is no built-in S/FTP support
- To prevent data corruption, we prevent multiple deployments from being active
  and mounted to the same service. This means that there will be a small amount
  of downtime when re-deploying a service that has a volume attached, even if there is a healthcheck endpoint configured
- Down-sizing a volume is not currently supported, but increasing size is supported
- Volume resizing is performed live without downtime - the underlying storage is expanded while your service continues running, and the filesystem automatically extends to utilize the additional space
- There is no file browser, or direct file download. To access your files,
  you must do so via the attached service's mount point
- Docker images that run as a non-root UID by default will have permissions issues when performing operations within an attached volume. If you are affected by this, you can set RAILWAY_RUN_UID=0 environment variable in your service.

## Support

Refer to the guide on how to use volumes for more details on how to use the feature.


# Uploading & serving
Source: https://docs.railway.com/storage-buckets/uploading-serving

Learn how to upload and serve files from Railway Storage Buckets.

Bucket egress is free. Service egress is not. If your service sends data to users or uploads files to a bucket, that traffic counts as service egress. The sections below explain these patterns and how to avoid unnecessary egress.

## Presigned URLs

Presigned URLs are temporary URLs that grant access to individual objects in your bucket for a specific amount of time. They can be created with any S3 client library and can live for up to 90 days.

Files served through presigned URLs come directly from the bucket and incur no egress costs.

## Serve files with presigned URLs

You can deliver files directly from your bucket by redirecting users to a presigned URL. This avoids egress costs from your service, as the service isn't serving the file itself.

Use-cases:
- Delivering user-uploaded assets like profile pictures
- Handing out temporary links for downloads
- Serving large files without passing them through your service
- Enforcing authorization before serving a file
- Redirecting static URLs to presigned URLs

## Serve files with a backend proxy

You can fetch a file in your backend and return it to the client. This gives you full control over headers, formatting, and any transformations. It does incur **service** egress, but it also lets you use CDN caching on your backend routes. Many frameworks support this pattern natively, especially for image optimization.

Use-cases:
- Transforming or optimizing images (resizing, cropping, compressing)
- Sanitizing files or validating metadata before returning them
- Taking advantage of CDN caching for frequently accessed files
- Web frameworks that already use a proxy for image optimization

## Upload files with presigned URLs

You can generate a presigned URL that lets the client upload a file directly to the bucket, without handling the upload in your service. Doing so prevents service egress and reduces memory consumption.

<Collapse title="Configuring CORS to upload files from a browser">

To upload a file from a browser frontend to the bucket, you need to configure CORS for your bucket and allow your frontend domain. You can do this with the aws CLI:

Make sure to replace your_access_key_id, your_secret_access_key, your-bucket_name and your_domain.tld.

</Collapse>

Similar to handling uploads through your service, be mindful that users may try to upload HTML, JavaScript, or other executable files. Treat all uploads as untrusted. Consider validating or scanning the file after the upload completes, and remove anything that shouldn't be served.

Use-cases:
- Uploading files from the browser
- Mobile apps uploading content directly
- Large file uploads where you want to avoid streaming through your service

## Upload files from a service

A service can upload directly to the bucket using the S3 API. This will incur service egress.

Use-cases:
- Background jobs generating files such as PDFs, exports, or thumbnails
- Writing logs or analytics dumps to storage
- Importing data from a third-party API and persisting it in the bucket

## Code Examples

import { s3 } from 'bun'

async function handleFileRequest(fileKey: string) {
  const isAuthorized = isUserAuthorized(currentUser, fileKey)
  if (!isAuthorized) throw unauthorized()

  const presignedUrl = s3.presign(fileKey, {
    expiresIn: 3600 // 1 hour
  })
  return Response.redirect(presignedUrl, 302)
}

// server-side
import { S3Client } from '@aws-sdk/client-s3'
import { createPresignedPost } from '@aws-sdk/s3-presigned-post'

async function prepareImageUpload(fileName: string) {
  const isAuthorized = isUserAuthorized(currentUser, fileKey)
  if (!isAuthorized) throw unauthorized()

  // The key under which the uploaded file will be stored.
  // Make sure that it's unique and users cannot override
  // each other's files.
  const Key = `user-uploads/${currentUser.id}/${fileName}`

  const { url, fields } = await createPresignedPost(new S3Client(), {
    Bucket: process.env.S3_BUCKET,
    Key,
    Expires: 3600,
    Conditions: [
      { bucket: process.env.S3_BUCKET },
      ['eq', '$key', Key],

      // restrict which content types can be uploaded
      ['starts-with', '$Content-Type', 'image/'],

      // restrict content length, to prevent users
      // from uploading suspiciously large files.
      // max 2 MB in this example.
      ['content-length-range', 5_000, 2_000_000],
    ],
  })

  return Response.json({ url, fields })
}

// client-side
async function uploadFile(file) {
  const res = await fetch('/prepare-image-upload', {
    method: 'POST',
    body: JSON.stringify({ fileName: file.name })
  })
  const { url, fields } = await res.json()

  const form = new FormData()
  Object.entries(fields).forEach(([key, value]) => {
    form.append(key, value)
  })
  form.append('Content-Type', file.type)
  form.append('file', file)

  await fetch(url, {
    method: 'POST',
    body: form
  })
}

AWS_ACCESS_KEY_ID=your_access_key_id \
AWS_SECRET_ACCESS_KEY=your_secret_access_key \
  aws s3api put-bucket-cors \
  --bucket your_bucket_name \
  --endpoint-url https://storage.railway.app \
  --cors-configuration '{
    "CORSRules": [
      {
        "AllowedHeaders": ["*"],
        "AllowedMethods": ["PUT","POST"],
        "AllowedOrigins": ["https://your_domain.tld"],
        "MaxAgeSeconds": 3000
      }
    ]
  }'

import { s3 } from 'bun'

async function generateReport() {
  const report = await createPdfReport()

  await s3.putObject("reports/monthly.pdf", report, {
    contentType: "application/pdf"
  })
}


# Billing
Source: https://docs.railway.com/storage-buckets/billing

Understand how Railway Storage Buckets are priced and billed.

Usage (GB-month) is calculated by averaging the day-to-day usages and rounding the final accumulation to the next whole number if it totaled a fractional amount (5.1 GB-month gets billed as 6 GB-month).

Buckets are currently only available in the Standard storage tier â there's no minimum storage retention and no data retrieval fees.

## Bucket egress VS. Service egress

Even though *buckets* don't charge for ingress or egress, buckets still live on the public network. When you upload files from your Railway services to your buckets, those *services* will incur egress usages, since you're uploading over the public network. Buckets are currently not available on the private network.

Note that service egress is not free. If your service sends data to users or uploads files to a bucket, that traffic counts as service egress.

## Billing examples

- If you stored **10 GBs for 30 days**, you'd get charged for **10 GB**-month.
- If you stored **10 GBs for 15 days** and **0 GB** for the next 15, your usage averages to **5 GB**-month.

## Plan limits

### Free plan

You can use up to **10 GB-month** each month on the free plan. Bucket usage counts against your $1 monthly credit. Once the credit is fully used, bucket access is suspended and files become unavailable, but your files will not be deleted. You can access your files again at the next billing cycle when credits refresh, or immediately if you upgrade to a paid plan.

### Trial plan

You can use up to **50 GB-month** during the trial. Bucket usage counts against your trial credits. When the trial ends, bucket access is suspended and files become unavailable. You can access your files again when you switch to the Free Plan or upgrade to a paid plan.

### Limited trial

Buckets are not available in the Limited Trial.

### Hobby

The Hobby Plan has a combined maximum storage capacity of **1TB**. Any uploads that would exceed this limit will fail.

### Pro

The Pro Plan has **unlimited** storage capacity.

## Usage limit

If you exceed your Hard Usage Limit, bucket access is suspended and files cannot be read or uploaded anymore. Existing stored data is still billed. You can access your files again once you raise or remove the Hard Limit, or when the next billing period starts.

## FAQ

<Collapse title="How are S3 API operations billed?">

All S3 API operations (PUT, GET, DELETE, LIST, HEAD, etc.) are free and unlimited on Railway Buckets.

In traditional S3 pricing, these are categorized as Class A operations (PUT, POST, COPY, LIST) and Class B operations (GET, HEAD), but on Railway, you don't need to worry about operation costs at all.

</Collapse>

<Collapse title="How is egress billed?">

Egress from buckets to the internet or to your services is free and unlimited.

Note that egress from your services to buckets (uploads) is billed at the standard public egress rate. Learn more about Bucket Egress vs. Service Egress.

</Collapse>


# ENOTFOUND redis.railway.internal
Source: https://docs.railway.com/databases/troubleshooting/enotfound-redis-railway-internal

Learn how to troubleshoot and fix the 'ENOTFOUND' redis.railway.internal error.

The error code ENOTFOUND means that your application could not resolve the redis.railway.internal hostname to an IP address when trying to connect to the Redis database.

## Why this error can occur

This error can occur for a few different reasons, but the main reason is because your application uses the ioredis package to connect to the Redis database, or uses a package that uses ioredis as a dependency such as bullmq.

By default, ioredis will only do an IPv4 (A record) lookup for the redis.railway.internal hostname.

In environments created before October 16th 2025, Railway's private network uses only IPv6 (AAAA records). In these legacy environments, the lookup will fail because the A records for redis.railway.internal do not exist.

**Note: New environments support both IPv4 and IPv6, so this specific cause is less likely to occur unless you are explicitly forcing an IPv4 connection in a legacy environment.**

Some other reasons that this error can occur would be -

- Your application and Redis database are in different projects.

- You are trying to connect to a Redis database locally with the private hostname and port.

For either of these reasons, the issue arises because the private network is scoped to a single environment within a project, and would not be accessible from your local machine or other projects.

If the Redis database is in the same project as your application, and you are not trying to connect to a Redis database locally, ioredis is the likely cause of the error.

## Solutions

The solution depends on the package you are using to connect to the Redis database, though the solution is the same for both.

### ioredis

#### Using ioredis directly in your application

ioredis has an option to do a dual stack lookup, which will try to resolve the redis.railway.internal hostname using both IPv4 and IPv6 addresses (A and AAAA records).

To enable this, in your REDIS_URL environment variable, you can set the family to 0 to enable dual stack lookup.

#### Using bullmq

Similarly, for bullmq since it uses ioredis as a dependency, you can set the family option to 0 in your connection object.

#### Other packages

Above we covered the two most common packages that can cause this error, but there are other packages that use ioredis as a dependency that may also cause this error.

If you are using a package that uses ioredis as a dependency, you can try to find a way to set the family option to 0 either in your connection object or in your REDIS_URL environment variable. Similar to the examples above.

### Redis database in a different project

Create a new Redis database in the same project as your application, and connect it to the Redis database using the private network as shown in the examples above.

Read about best pracices to get the most out of the platform here.

### Connecting to a Redis database locally

The easiest way to connect to a Redis database locally is to use the public network.

You can do this is by using the REDIS_PUBLIC_URL environment variable to connect to the Redis database.

## Code Examples

import Redis from "ioredis";

const redis = new Redis(process.env.REDIS_URL + "?family=0");

const ping = await redis.ping();

import { Queue } from "bullmq";

const redisURL = new URL(process.env.REDIS_URL);

const queue = new Queue("Queue", {
  connection: {
    family: 0,
    host: redisURL.hostname,
    port: redisURL.port,
    username: redisURL.username,
    password: redisURL.password,
  },
});

const jobs = await queue.getJobs();

console.log(jobs);

import Redis from "ioredis";

const redis = new Redis(process.env.REDIS_PUBLIC_URL);

const ping = await redis.ping();



# Networking
Source: https://docs.railway.com/networking

# Specs & limits
Source: https://docs.railway.com/networking/public-networking/specs-and-limits

Technical specifications and rate limits for Railway's public networking.



## Technical specifications

| Category                 | Key Information                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DNS/Domain Names**     | - Support for domains, subdomains, and wildcard domains.<br/>- Subdomains and wildcards cannot overlap (foo.hello.com cannot exist with *.hello.com unless owned by the same service).<br/>- Root domains need a DNS provider with ALIAS records or CNAME flattening.<br/>- Unicode domains should be PUNYcode encoded.<br/>- Non-public/internal domain names are not supported.                                                          |
| **Certificate Issuance** | - Railway attempts to issue a certificate for **up to 72 hours** after domain creation before failing.<br/>- Certificates are expected to be issued within an hour.                                                                                                                                                                                                                                                                            |
| **TLS**                  | - Support for TLS 1.2 and TLS 1.3 with specific cipher sets.<br/>- Certificates are valid for 90 days and renewed when 30 days of validity remain.                                                                                                                                                                                                                                                                                                               |
| **Edge Traffic**         | - Support for HTTP/1.1.<br/>- Support for websockets over HTTP/1.1.<br/>- Proxy Keep-Alive timeout of 60 seconds (1 minute).<br/>- Max 32 KB Combined Header Size<br/>- Max duration of 15 minutes for HTTP requests.                                                                                                                                                                                                                          |
| **Request Headers**      | - X-Real-IP for identifying client's remote IP.<br/>- X-Forwarded-Proto always indicates https.<br/>- X-Forwarded-Host for identifying the original host header.<br/>- X-Railway-Edge for identifying the edge region that handled the request.<br/>- X-Request-Start for identifying the time the request was received (Unix milliseconds timestamp).<br/>- X-Railway-Request-Id for correlating requests against network logs. |
| **Requests**             | - Inbound traffic must be TLS-encrypted<br/>- HTTP GET requests to port 80 are redirected to HTTPS.<br/>- HTTP POST requests to port 80 are redirected to HTTPS as GET requests.<br/>- SNI is required for correct certificate matching.                                                                                                                                                                                                       |

## Rate limits

To ensure the integrity and performance of the Railway network, we enforce the following limits for all services.

| Category                    | Limit                         | Description                                               |
| --------------------------- | ----------------------------- | --------------------------------------------------------- |
| **Maximum Connections**     | 10,000 concurrent connections | The number of concurrent connections.                     |
| **HTTP Requests/Sec**       | 11,000~ RPS                   | The number of HTTP requests to a given domain per second. |
| **Requests Per Connection** | 10,000 requests               | The number of requests each connection can make.          |

If your application requires higher limits, please don't hesitate to reach out to us at team@railway.com.

## Traffic types

We currently support HTTP and HTTP2 traffic from the internet to your services.

All traffic must be HTTPS and use TLS 1.2 or above, and TLS SNI is mandatory for requests.

- Plain HTTP GET requests will be redirected to HTTPS with a 301 response.
- Plain HTTP POST requests will be converted to GET requests.

For services that require TCP traffic, like databases, we also have TCP Proxy support.

## SSL certificates

We provide LetsEncrypt SSL certificates using RSA 2048bit keys. Certificates are valid for 90 days and are automatically renewed 2 months into their life.

Certificate issuance should happen within an hour of your DNS being updated with the values we provide.

For proxied domains (Cloudflare orange cloud), we may not always be able to issue a certificate for the domain, but Cloudflare to Railway traffic will be encrypted with TLS using the default Railway *.up.railway.app certificate.

## Ddos protection

Railway Metal infrastructure is built to mitigate attacks at network layer 4 and below, however we do not provide protection on the application layer. If you need WAF functionality, we recommend using Cloudflare alongside Railway.


# Library configuration
Source: https://docs.railway.com/networking/private-networking/library-configuration

Configure libraries and frameworks for Railway's private networking.



## Node.js libraries

### ioredis

ioredis is a Redis client for node.js, commonly used for connecting to Redis from a node application.

When initializing a Redis client using ioredis, you must specify family=0 in the connection string to support connecting to both IPv6 and IPv4 endpoints:

<a href="https://www.npmjs.com/package/ioredis" target="_blank">ioredis docs</a>

### bullmq

bullmq is a message queue and batch processing library for node.js, commonly used for processing jobs in a queue.

When initializing a bullmq client, you must specify family: 0 in the connection object to support connecting to both IPv6 and IPv4 Redis endpoints:

<a href="https://docs.bullmq.io/" target="_blank">bullmq docs</a>

### Hot-shots

hot-shots is a StatsD client for node.js, which can be used to ship metrics to a DataDog agent for example. When initializing a StatsD client using hot-shots, you must specify that it should connect over IPv6:

<a href="https://www.npmjs.com/package/hot-shots" target="_blank">hot-shots docs</a>

## Go libraries

### Fiber

fiber is a web framework for Go. When configuring your Fiber app, you should set the Network field to tcp to have it listen on IPv6 as well as IPv4:

<a href="https://docs.gofiber.io/api/fiber#:~:text=json.Marshal-,Network,-string" target="_blank">Fiber docs</a>

## Docker images

### MongoDB

If you are creating a service using the official Mongo Docker image from Docker Hub and would like to connect to it over the private network, you must start the container with options to instruct the Mongo instance to listen on IPv6. Set this in your Start Command:

**Note:** The official MongoDB template provided by Railway is already deployed with this Start Command.

## Adding more libraries

If you encounter a library that requires specific configuration for Railway's private networking, please let us know on the <a href="https://discord.gg/railway" target="_blank">Railway Discord</a> or submit a PR to the documentation.

## Code Examples

import Redis from "ioredis";

const redis = new Redis(process.env.REDIS_URL + "?family=0");

const ping = await redis.ping();

import { Queue } from "bullmq";

const redisURL = new URL(process.env.REDIS_URL);

const queue = new Queue("Queue", {
  connection: {
    family: 0,
    host: redisURL.hostname,
    port: redisURL.port,
    username: redisURL.username,
    password: redisURL.password,
  },
});

const jobs = await queue.getJobs();

console.log(jobs);

const StatsD = require("hot-shots");

const statsdClient = new StatsD({
  host: process.env.AGENT_HOST,
  port: process.env.AGENT_PORT,
  protocol: "udp",
  cacheDns: true,
  udpSocketOptions: {
    type: "udp6",
    reuseAddr: true,
    ipv6Only: true,
  },
});

app := fiber.New(fiber.Config{
    Network:       "tcp",
    ServerHeader:  "Fiber",
    AppName: "Test App v1.0.1",
})

docker-entrypoint.sh mongod --ipv6 --bind_ip ::,0.0.0.0


# Working with Domains
Source: https://docs.railway.com/networking/domains/working-with-domains

Learn how to configure public and private domains for your Railway services.



## Public domains

Public domains expose your services to the internet. Railway offers two options:

- **Railway-provided domains** - Auto-generated *.up.railway.app domains for quick setup
- **Custom domains** - Bring your own domain with automatic SSL certificate provisioning

### Railway-provided domains

Railway services don't obtain a domain automatically, but it is easy to set one up.

To assign a domain to your service, go to your service's settings, find the Networking -> Public Networking section, and choose Generate Domain.

#### Automated prompt

If Railway detects that a deployed service is listening correctly, you will see a prompt on the service tile in the canvas, and within the service panel.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1654560212/docs/add-domain_prffyh.png"
alt="Screenshot of adding Service Domain"
layout="responsive"
width={1396} height={628} quality={80} />

Simply follow the prompts to generate a domain and your app will be exposed to the internet.

**Don't see the Generate Domain Button?**

If you have previously assigned a TCP Proxy to your service, you will not see the Generate Domain option. You must remove the TCP Proxy (click the Trashcan icon), then you can add a domain.

### Custom domains

Custom domains can be added to a Railway service and once setup we will automatically issue an SSL certificate for you.

1. Navigate to the Settings tab of your desired service.

2. Click + Custom Domain in the Public Networking section of Settings

3. Type in the custom domain (wildcard domains are supported, see below for more details)

   You will be provided with a CNAME domain to use, e.g., g05ns7.up.railway.app.

4. In your DNS provider (Cloudflare, DNSimple, Namecheap, etc), create a CNAME record with the CNAME value provided by Railway.

5. Wait for Railway to verify your domain. When verified, you will see a green check mark next to the domain(s) -

   <Image
   src="https://res.cloudinary.com/railway/image/upload/v1654563209/docs/domains_uhchsu.png"
   alt="Screenshot of Custom Domain"
   layout="responsive"
   width={1338} height={808} quality={80} />

   You will also see a Cloudflare proxy detected message if we have detected that you are using Cloudflare.

   **Note:** Changes to DNS settings may take up to 72 hours to propagate worldwide.

#### Important considerations

- Freenom domains are not allowed and not supported.
- The Trial Plan is limited to 1 custom domain. It is therefore not possible to use both yourdomain.com and www.yourdomain.com as these are considered two distinct custom domains.
- The Hobby Plan is limited to 2 custom domains per service.
- The Pro Plan is limited to 20 domains per service by default. This limit can be increased for Pro users on request, simply reach out to us via a private thread.

### Wildcard domains

Wildcard domains allow for flexible subdomain management. There are a few important things to know when using them -

- Ensure that the CNAME record for authorize.railwaydns.net is not proxied by your provider (eg: Cloudflare). This is required for the verification process to work.

- Wildcards cannot be nested (e.g., \*.\*.yourdomain.com).

- Wildcards can be used for any subdomain level (e.g., *.example.com or *.subdomain.example.com).

#### Subdomains

E.g. *.example.com

- Make sure Universal SSL is enabled.

- Enable Full SSL/TLS encryption.

- Add CNAME records for the wildcard subdomain.

#### Nested subdomains

E.g. *.nested.example.com

- Disable Universal SSL.

- Purchase Cloudflare's Advanced Certificate Manager.

- Enable Edge Certificates.

- Enable Full SSL/TLS encryption.

- Add CNAME records for the wildcard nested subdomain.

When you add a wildcard domain, you will be provided with two domains for which you should add two CNAME records -

<Image
src="https://res.cloudinary.com/railway/image/upload/v1679693511/wildcard_domains_zdguqs.png"
alt="Screenshot of Wildcard Domain"
layout="responsive"
width={1048} height={842} quality={80} />

One record is for the wildcard domain, and one for the \_acme-challenge. The \_acme-challenge CNAME is required for Railway to issue the SSL Certificate for your domain.

#### Wildcard domains on Cloudflare

If you have a wildcard domain on Cloudflare, you must:

- Turn off Cloudflare proxying on the _acme-challenge record (disable the orange cloud)

- Enable Cloudflare's Universal SSL

### Target ports

Target Ports, or Magic Ports, correlate a single domain to a specific internal port that the application listens on, enabling you to expose multiple HTTP ports through the use of multiple domains.

Example -

https://example.com/ â :8080

https://management.example.com/ â :9000

When you first generate a Railway-provided domain, if your application listens on a single port, Railway's magic automatically detects and sets it as the domain's target port. If your app listens on multiple ports, you're provided with a list to choose from.

When you add a custom domain, you're given a list of ports to choose from, and the selected port will handle all traffic routed to the domain. You can also specify a custom port if needed.

These target ports inform Railway which public domain corresponds to each internal port, ensuring that traffic from a specific domain is correctly routed to your application.

<Image src="https://res.cloudinary.com/railway/image/upload/v1743196226/docs/custom-domain_ulvgap.png"
alt="Screenshot of target port selection on a custom domain"
layout="intrinsic"
width={1200} height={1035}
quality={100} />

You can change the automatically detected or manually set port at any time by clicking the edit icon next to the domain.

### Adding a root domain

When adding a root or apex domain to your Railway service, you must ensure that you add the appropriate DNS record to the domain within your DNS provider. At this time, Railway supports <a href="https://developers.cloudflare.com/dns/cname-flattening/" target="_blank">CNAME Flattening</a> and dynamic ALIAS records.

**Additional context**

Generally, direct CNAME records at the root or apex level are incompatible with DNS standards (which assert that you should use an "A" or "AAAA" record). However, given the dynamic nature of the modern web and PaaS providers like Railway, some DNS providers have incorporated workarounds enabling CNAME-like records to be associated with root domains.
_Check out <a href="https://www.ietf.org/rfc/rfc1912.txt#:~:text=root%20zone%20data).-,2.4%20CNAME%20records,-A%20CNAME%20record" target="_blank">RFC 1912</a> if you're interested in digging into this topic._

**Choosing the correct record type**

The type of record to create is entirely dependent on your DNS provider. Here are some examples -

- <a href="https://developers.cloudflare.com/dns/zone-setups/partial-setup" target="_blank">Cloudflare CNAME</a> - Simply set up a CNAME record for your root domain in Cloudflare, and they take care of the rest under the hood. Refer to <a href="https://support.cloudflare.com/hc/en-us/articles/205893698-Configure-Cloudflare-and-Heroku-over-HTTPS" target="_blank">this guide</a> for more detailed instructions.
- <a href="https://support.dnsimple.com/articles/domain-apex-heroku/" target="_blank">DNSimple ALIAS</a> - Set up a dynamic ALIAS in DNSimple for your root domain.
- <a href="https://www.namecheap.com/support/knowledgebase/article.aspx/9646/2237/how-to-create-a-cname-record-for-your-domain/" target="_blank">Namecheap CNAME</a> - Set up a CNAME in Namecheap for your root domain.
- <a href="https://bunny.net/blog/how-aname-dns-records-affect-cdn-routing/" target="_blank">bunny.net</a> - Set up a ANAME in bunny.net for your root domain.

In contrast there are many nameservers that don't support CNAME flattening or dynamic ALIAS records -

- <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register-other-dns-service.html" target="_blank">AWS Route 53</a>
- <a href="https://learn.microsoft.com/en-us/answers/questions/2338846/cname-record-root" target="_blank">Azure DNS</a>
- <a href="https://support.hostinger.com/en/articles/1696789-how-to-change-nameservers-at-hostinger" target="_blank">Hostinger</a>
- <a href="https://www.godaddy.com/en-ca/help/edit-my-domain-nameservers-664" target="_blank">GoDaddy</a>
- <a href="https://www.namesilo.com/support/v2/articles/domain-manager/dns-manager" target="_blank">NameSilo</a>
- <a href="https://dns.he.net/" target="_blank">Hurricane Electric</a>
- <a href="https://support.squarespace.com/hc/en-us/articles/4404183898125-Nameservers-and-DNSSEC-for-Squarespace-managed-domains#toc-open-the-domain-s-advanced-settings" target="_blank">SquareSpace</a>

**Workaround - Changing your Domain's Nameservers**

If your DNS provider doesn't support CNAME Flattening or dynamic ALIAS records at the root, you can also change your domain's nameservers to point to Cloudflare's nameservers. This will allow you to use a CNAME record for the root domain. Follow the instructions listed on Cloudflare's documentation to <a href="https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/" target="_blank">change your nameservers</a>.

### Adding a root domain with www subdomain to Cloudflare

If you want to add your root domain (e.g., mydomain.com) and the www. subdomain to Cloudflare and redirect all www. traffic to the root domain:

1. Create a Custom Domain in Railway for your root domain (e.g., mydomain.com). Copy the value field. This will be in the form: abc123.up.railway.app.
2. Add a CNAME DNS record to Cloudflare:
   - Name â @.
   - Target â the value field from Railway.
   - Proxy status â on, should display an orange cloud.
   - Note: Due to domain flattening, Name will automatically update to your root domain (e.g., mydomain.com).
3. Add another CNAME DNS record to Cloudflare:
   - Name â www.
   - Target â @
   - Proxy status: â on, should display an orange cloud.
   - Note: Cloudflare will automatically change the Target value to your root domain.
4. Enable Full SSL/TLS encryption in Cloudflare:
   - Go to your domain on Cloudflare.
   - Navigate to SSL/TLS -> Overview.
   - Select Full. **Not** Full (Strict) **Strict mode will not work as intended**.
5. Enable Universal SSL in Cloudflare:
   - Go to your domain on Cloudflare.
   - Navigate to SSL/TLS -> Edge Certificates.
   - Enable Universal SSL.
6. After doing this, you should see Cloudflare proxy detected on your Custom Domain in Railway with a green cloud.
7. Create a Bulk Redirect in Cloudflare:
   - Go to your Cloudflare dashboard.
   - Navigate to Bulk Redirects.
   - Click Create Bulk Redirect List.
   - Give it a name, e.g., www-redirect.
   - Click Or, manually add URL redirects.
   - Add a Source URL: https://www.mydomain.com.
   - Add Target URL: https://mydomain.com with status 301.
   - Tick all the parameter options: (Preserve query string, Include subdomains, Subpath matching, Preserve path suffix)
   - Click Next, then Save and Deploy.

**Note:** DNS changes may take some time to propagate. You may want to refresh your DNS cache by using commands like ipconfig /flushdns on Windows or dscacheutil -flushcache on macOS. Testing the URLs in an incognito window can also help verify changes.

### SSL certificates

Once a custom domain has been correctly configured, Railway will automatically generate and apply a Let's Encrypt certificate. This means that any custom domain on Railway will automatically be accessible via https://.

We provide LetsEncrypt SSL certificates using RSA 2048bit keys. Certificates are valid for 90 days and are automatically renewed when 30 days of validity remain.

Certificate issuance should happen within an hour of your DNS being updated with the values we provide.

For proxied domains (Cloudflare orange cloud), we may not always be able to issue a certificate for the domain, but Cloudflare to Railway traffic will be encrypted with TLS using the default Railway *.up.railway.app certificate.

#### External SSL certificates

We currently do not support external SSL certificates since we provision one for you.

### Cloudflare configuration

If you have proxying enabled on Cloudflare (the orange cloud), you MUST set your SSL/TLS settings to **Full** -- Full (Strict) **will not work as intended**.

<Image src="https://res.cloudinary.com/railway/image/upload/v1631917785/docs/cloudflare_zgeycj.png"
alt="Screenshot of Custom Domain"
layout="responsive"
width={1205} height={901} quality={80} />

If proxying is not enabled, Cloudflare will not associate the domain with your Railway project. In this case, you will encounter the following error message:

Also note that if proxying is enabled, you can NOT use a domain deeper than a first level subdomain without Cloudflare's Advanced Certificate Manager. For example, anything falling under \*.yourdomain.com can be proxied through Cloudflare without issue, however if you have a custom domain under \*.subdomain.yourdomain.com, you MUST disable Cloudflare Proxying and set the CNAME record to DNS Only (the grey cloud), unless you have Cloudflare's Advanced Certificate Manager.

---

## Private domains

Private domains enable service-to-service communication within Railway's private network. Every service automatically gets an internal DNS name under the railway.internal domain.

### How private DNS works

By default, all projects have private networking enabled and services will get a DNS name in the format:

For example, if you have a service called api, its internal hostname would be api.railway.internal.

For new environments (created after October 16, 2025), this DNS name resolves to both internal IPv4 and IPv6 addresses. Legacy environments resolve to IPv6 only.

### Using private domains

To communicate with a service over the private network, use the internal hostname and the port on which the service is listening:

**Note:** Use http (not https) for internal communication - traffic stays within the private network.

### Using reference variables

You can use reference variables to dynamically reference another service's private domain:

Then in your code:

### Changing the service name

Within the service settings, you can change the service name which updates the DNS name, e.g., api-1.railway.internal â api-2.railway.internal.

The root of the domain, railway.internal, is static and **cannot** be changed.

### Private domain scope

The private network exists in the context of a project and environment:

- Services in one project/environment **cannot** communicate with services in another project/environment over the private network.
- Client-side requests from browsers **cannot** reach the private network - they must go through a public domain.

For complete information on configuring services for private networking, see the Private Networking guide.

## Troubleshooting

Having trouble with your domain configuration? Check out the Troubleshooting guide or reach out on the <a href="https://discord.gg/railway" target="_blank">Railway Discord</a>.

## Code Examples

ERR_TOO_MANY_REDIRECTS

<service-name>.railway.internal

// Example: Frontend service calling an API service
app.get("/fetch-data", async (req, res) => {
  axios.get("http://api.railway.internal:3000/data").then(response => {
    res.json(response.data);
  });
});

BACKEND_URL=http://${{api.RAILWAY_PRIVATE_DOMAIN}}:${{api.PORT}}

app.get("/fetch-data", async (req, res) => {
  axios.get(`${process.env.BACKEND_URL}/data`).then(response => {
    res.json(response.data);
  });
});


# Railway Domains
Source: https://docs.railway.com/networking/domains/railway-domains

Purchase and manage domains directly within Railway.



## Search for a domain

Navigate to railway.com/domains or click **Buy a Domain** from a service's networking settings.

- Real-time search shows availability and pricing
- Describe what you're building to get AI-powered domain suggestions
- Over 250 TLDs available (.com, .io, .dev, .app, .ai, .co, and more)

## Purchase a domain

Select a domain, confirm the price, and purchase with your existing payment method.

- Domains are registered for one year (some TLDs like .ai require a two-year minimum)
- WHOIS privacy enabled by default
- Auto-renewal enabled by default
- Railway is listed as the registrant contact and handles all registry communications on your behalf
- When purchased from a service, the domain is automatically attached and configured

## Manage domains

View all purchased domains at railway.com/workspace/domains.

- Expiry/renewal dates, attached services, and payment status
- Toggle auto-renewal (workspace admins)
- Connect a domain to a service or subdomain at any time

## DNS

Railway fully manages DNS for purchased domains. Records are created and maintained automatically, with no manual configuration required.

If you need manual DNS control, purchase from an external registrar and use custom domains instead.

## Billing

Domain subscriptions are separate from your workspace subscription.

- Priced at cost, rounded to dollar
- First-year price may differ from the renewal price
- You receive a notification before an upcoming renewal
- Auto-renewal charges approximately 30 days before expiration
- If payment fails, Railway retries up to three times before the domain expires

## FAQ

Common questions about Railway Domains.

<Collapse title="Can I transfer a domain between workspaces?">
Not yet. This capability is planned.
</Collapse>

<Collapse title="Can I transfer a domain out of Railway?">
Not available through self-service. Domains must have been registered for at least 60 days before they can be transferred out. Contact support if you need this.
</Collapse>

<Collapse title="Which TLDs are available?">
Over 250 popular TLDs. No restricted or country-code TLDs requiring local presence.
</Collapse>

<Collapse title="Can I buy a domain without attaching it to a service?">
Yes. Purchase a domain and connect it to a service later.
</Collapse>

<Collapse title="What happens if renewal payment fails?">
Railway retries payment up to three times before the domain expires.
</Collapse>

<Collapse title="Can I manually configure DNS records?">
No. DNS is fully managed by Railway. Use an external registrar with custom domains if you need manual DNS control.
</Collapse>

<Collapse title="Who is the registrant contact for my domain?">
Railway is listed as the registrant contact. We handle all registry and ICANN communications on your behalf.
</Collapse>


# TCP proxy
Source: https://docs.railway.com/networking/tcp-proxy

Learn how to proxy TCP traffic to a service on Railway.



## How it works

Enabling TCP Proxy on a service requires specification of a port to which the traffic should be proxied. Railway then generates a domain and proxy port, and all traffic sent to domain:port will be proxied to the service.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743194081/docs/tcp-proxy_edctub.png"
alt="Screenshot of TCP proxy configuration"
layout="responsive"
width={1200} height={822} quality={100} />

## Setting up TCP proxy

To create a TCP proxy:

1. Navigate to your service's Settings
2. Find the Networking section
3. Click on TCP Proxy
4. Enter the internal port your service listens on
5. Railway will generate a proxy domain and port (e.g., shuttle.proxy.rlwy.net:15140)

## Load balancing

Incoming traffic will be distributed across all replicas in the closest region using a random load balancing algorithm.

## Use cases

TCP Proxy is commonly used for:

- **Databases** - Expose PostgreSQL, MySQL, Redis, or other databases for external access
- **Game servers** - Allow players to connect directly via TCP
- **Custom protocols** - Any service using a non-HTTP protocol
- **IoT devices** - Connect devices that communicate over raw TCP

## Using a custom domain for TCP proxying

You can use your own domain instead of Railway's provided TCP proxy domain.

To set this up:

1. Create a TCP proxy in your service settings. Railway will provide you with a proxy domain and port (e.g., shuttle.proxy.rlwy.net:15140).

2. In your DNS provider, create a CNAME record pointing to the Railway-provided TCP proxy domain (without the port).

   For example, if Railway provides shuttle.proxy.rlwy.net:15140:
   - **Name**: db.yourdomain.com (or your preferred subdomain)
   - **Target**: shuttle.proxy.rlwy.net

3. Connect to your service using your custom domain with the Railway-provided port (e.g., db.yourdomain.com:15140).

**Note:** The port number is provided by Railway and must be used when connecting. Only the hostname is replaced with your custom domain.

**Caveats:**
- If using Cloudflare, proxying must be disabled (DNS only, grey cloud).
- If your client validates or looks for a specific hostname in the connection, it may fail when using a custom domain.

## Using HTTP and TCP together

Railway supports exposing both HTTP and TCP over public networking in a single service. If you have a domain assigned, you will still see the option to enable TCP Proxy, and vice-versa.

## TCP with private networking

TCP Proxy can also be used in conjunction with Private Networking for internal service-to-service communication. Services within the same project or environment can communicate over TCP using internal DNS names without exposing traffic to the public internet.

## Troubleshooting

Having issues with your TCP proxy? Check out the Troubleshooting guide or reach out on the <a href="https://discord.gg/railway" target="_blank">Railway Discord</a>.


# Outbound networking
Source: https://docs.railway.com/networking/outbound-networking

Learn about outbound networking features and email delivery options on Railway.



## Email delivery

SMTP is only available on the Pro plan and above.

Free, Trial, and Hobby plans must use transactional email services with HTTPS APIs. SMTP is disabled on these plans to prevent spam and abuse. However, even when SMTP is available, we recommend transactional email services with HTTPS APIs for all plans due to their enhanced features and analytics.

<Banner variant="info">Upon upgrading to Pro, please re-deploy your service that needs to use SMTP for the changes to take effect.</Banner>

### Email service examples

Here are examples of transactional email services you can use:

**Note:** These services are required for Free, Trial, and Hobby plans since outbound SMTP is disabled.

- Resend - **Railway's recommended approach**
- SendGrid
- Mailgun
- Postmark

These services provide detailed analytics and robust APIs designed for modern applications. They also work on all Railway plans since they use HTTPS instead of SMTP.

### Debugging SMTP issues

If you are experiencing issues with SMTP on the Pro plan, please the follow the steps below to help us diagnose the problem:

1. First, ensure that you have tried re-deploying your service

2. SSH into your service using the Railway CLI:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1757952518/docs/smtp-copy-ssh_qtczce.png"
alt="Screenshot of SSH into your service"
layout="responsive"
width={767} height={729} quality={100} />

3. Copy-paste this command and change the SMTP_HOST to the host you're trying to connect to:

4. Execute the command. You should see output similar to this:

Example:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1757952876/docs/smtp-exec-cmd_ytqx7u.png"
alt="Screenshot of executing debug command"
layout="responsive"
width={767} height={729} quality={100} />

Replace smtp.resend.com above with your SMTP host.

5. If any of the ports are unreachable, please contact your email provider to
ensure that they are not blocking connections from Railway's IPs. Port 2525 is
a non-standard SMTP port that may be blocked on popular email providers, so
2525 being unreachable is not an issue

6. Otherwise, please reach out to us at Central Station
and share the output of the command for further assistance

## Static outbound IPs

Railway offers Static Outbound IPs for Pro plan customers who need consistent IP addresses for firewall whitelisting or third-party integrations.

## Outbound ipv6

Railway does not currently support outbound IPv6. Any IPv6 request will fail showing "Network is unreachable" or ENETUNREACH.

## Related features

- Static Outbound IPs - Assign permanent outbound IP addresses
- Private Networking - Internal service communication
- Public Networking - Inbound traffic to your services

## Code Examples

SMTP_HOST="$REPLACE_THIS_WITH_YOUR_SMTP_HOST" bash -c '
for port in 25 465 587 2525; do
  timeout 1 bash -c "</dev/tcp/$SMTP_HOST/$port" 2>/dev/null && \
    echo "$SMTP_HOST port $port reachable" || \
    echo "$SMTP_HOST port $port unreachable"
done
'

smtp.yourhost.com port 25 reachable
smtp.yourhost.com port 465 reachable
smtp.yourhost.com port 587 reachable
smtp.yourhost.com port 2525 reachable


# Static outbound IPs
Source: https://docs.railway.com/networking/static-outbound-ips

Learn how to enable static outbound IPs on Railway.



## Use cases

This feature may be useful to you if you're using a third-party service provider or firewall which requires you to whitelist which IP addresses your services will be connecting from, such as MongoDB Atlas.

The IPv4 address assigned to your service through this feature **cannot** be used to receive inbound traffic.

## Enabling static outbound IPs

Customers on the Pro plan can enable Static Outbound IPs for any service they wish.

1. Navigate to the Settings tab of your desired service
2. Toggle Enable Static IPs in the Networking section of Settings
3. You will be presented with an IPv4 address which is tied to the region your service is deployed in
4. The Static IP will be used by your service after the next deploy

<Image
  src="https://res.cloudinary.com/railway/image/upload/v1716858865/docs/d6u20lrvxmlc8rfu91rx.png"
  layout="responsive"
  alt="Static IPs"
  width={1328} height={710} quality={80} />

## Caveats

- There is no guarantee that the IPv4 address assigned to your service is dedicated. It may be shared with other customers.
- The IP address cannot be used for inbound traffic.
- If you wish to move your service to a different region, the IP address will change.


# Edge networking
Source: https://docs.railway.com/networking/edge-networking

Learn how Railway's global edge network routes traffic to your deployments



## Edge network architecture

### How anycast works

Railway's edge network uses anycast routing. With anycast, the same IP address is advertised from multiple geographic locations. When a user makes a request to your Railway service:

1. Their DNS query resolves to Railway's anycast IP addresses
2. Internet routing (BGP) automatically directs the request to the **nearest edge location** based on network topology
3. The edge proxy terminates TLS, processes the request, and forwards it to your deployment

The key insight is that **"nearest" is determined by network topology, not geographic distance**. A user in one city might be routed to an edge location in a different region if that path has better network connectivity.

### Edge regions VS deployment regions

Railway operates in four locations: **US West**, **US East**, **Europe West**, and **Asia Southeast**. Each location can serve as both an entry point for traffic (edge region) and a deployment target for your applications (deployment region).

You choose which locations to deploy your app to, but all edge regions are available automatically. Your users always enter Railway at the location nearest to them, regardless of where your app is deployed.

For any given request, traffic enters at the nearest edge region, then routes internally to the nearest deployment region where your app is running. If your app is deployed in multiple locations, traffic is routed to the closest one. If your app is only in one location, traffic routes there regardless of where it entered.

### Request flow

When a request reaches your Railway service, it follows this path:

1. **User to Edge**: Anycast routing directs traffic to the nearest edge location
2. **Edge Processing**: The edge proxy (tcp-proxy) terminates TLS, adds headers, and looks up routing information
3. **Internal Routing**: Traffic is forwarded over Railway's internal network to your deployment
4. **Service Response**: Your service processes the request and the response follows the reverse path

## Understanding the x-Railway-edge header

Every HTTP request to your Railway service includes the X-Railway-Edge header, which identifies which edge location handled the request.

### Header format

The header value follows the format: railway/{region-identifier}

| Header | Region | Location |
| ------ | ------ | -------- |
| railway/us-west2 | US West | California, USA |
| railway/us-east4-eqdc4a | US East | Virginia, USA |
| railway/europe-west4-drams3a | Europe West | Amsterdam, Netherlands |
| railway/asia-southeast1-eqsg3a | Southeast Asia | Singapore |

### What it tells you

The X-Railway-Edge header indicates:
- Which edge location received and processed the incoming request
- The geographic region where TLS was terminated
- The entry point into Railway's network for that specific request

### What it does not tell you

The header does **not** indicate:
- Where your deployment is running (use Deployment Regions for that)
- The user's actual geographic location
- The optimal routing path

### Accessing the header

You can see this header in your deployment's HTTP logs, or read it programmatically in your application like any other HTTP request header.

## Why traffic hits "wrong" regions

A common question from users is: "Why does X-Railway-Edge show a different region than where I'm located or where my deployment runs?" This is usually expected behavior.

### Anycast routes to nearest edge, not deployment

The edge region is determined by anycast routing, which optimizes for network path, not geographic proximity. Your deployment region is a separate configuration that determines where your application runs.

**Example**: A user in Chicago might see X-Railway-Edge: railway/us-east4-eqdc4a even though their service is deployed in us-west2. This is normal - the request entered via the US East edge (nearest by network path) and was then routed internally to the US West deployment.

### Isp and network factors

Internet routing depends on:
- Your ISP's peering agreements
- Network congestion and availability
- BGP routing decisions made by intermediate networks

These factors can cause traffic to take unexpected paths that don't align with geographic intuition.

### Cloudflare and CDN influence

If you're using Cloudflare or another CDN in front of Railway:

1. The user's request first hits Cloudflare's edge
2. Cloudflare forwards the request to Railway from its edge location
3. Railway's anycast routes based on where Cloudflare's request originates, not the end user

This can result in X-Railway-Edge showing a region that matches Cloudflare's edge location rather than the end user's location. This is expected behavior when using a CDN.

### Vpns and proxies

Users connecting through VPNs or corporate proxies will have their traffic routed based on the VPN/proxy exit point, not their actual location.

## Diagnosing routing issues

### When edge region mismatch is expected

These scenarios are **normal** and don't require investigation:

- X-Railway-Edge shows a different region than your deployment region
- X-Railway-Edge varies for users in the same geographic area
- X-Railway-Edge doesn't match your users' expected locations when using a CDN
- Occasional variation in which edge handles requests

### When to investigate

Consider reaching out to support if:

- All traffic consistently routes to a single, distant edge when you expect geographic distribution
- You see significantly higher latency than expected for your users' locations
- Traffic routing changes suddenly and dramatically without any configuration changes

### Diagnostic steps

1. **Check your current routing**: Visit Railway's routing info page to see which edge region your requests are hitting

2. **Check the header**: Inspect X-Railway-Edge in your application logs or by making test requests

3. **Run traceroute**: Test network paths to Railway's anycast IP
   

4. **Compare from multiple locations**: Use tools like globalping.io to test routing from different geographic locations

5. **Check your CDN configuration**: If using Cloudflare or similar, verify your DNS and proxy settings

### Contacting support

If you need to report a routing issue, include:
- The X-Railway-Edge header value from affected requests
- Your deployment ID (found in the Railway dashboard)
- Traceroute results to 66.33.22.11
- The geographic location where the issue is observed
- Whether you're using a CDN or proxy

## Related documentation

- Deployment Regions - Configure where your services run
- Public Networking - Overview of public networking features
- Network Diagnostics - Tools for troubleshooting network issues
- TCP Proxy - Proxy TCP traffic to your services

## Code Examples

User â ISP â Internet (BGP) â Nearest Edge
  â Internal Routing â Deployment Region â Your Service

traceroute 66.33.22.11


# SSL
Source: https://docs.railway.com/networking/troubleshooting/ssl

Learn how to diagnose and fix common SSL certificate issues on Railway.



## How Railway SSL works

When you add a domain to your service, Railway automatically:

1. Initiates a certificate request with Let's Encrypt
2. Completes domain validation challenges
3. Issues and installs the certificate
4. Renews certificates automatically when 30 days of validity remain (certificates are valid for 90 days)

Certificate issuance typically completes within an hour, though it can take up to 72 hours in some cases.

## Quick reference

| Symptom | Section |
|---------|---------|
| Certificate stuck on "Validating Challenges" | Certificate Stuck on "Validating Challenges" |
| ERR_TOO_MANY_REDIRECTS | Cloudflare SSL Errors |
| Error 526: Invalid SSL Certificate | Cloudflare SSL Errors |
| Error 525: SSL Handshake Failed | Cloudflare SSL Errors |
| SSL works for some users but not others | Connection Issues for Some Users |
| Certificate shows *.up.railway.app | Certificate Shows Wrong Domain |

## Before you troubleshoot

Many SSL issues are actually browser cache issues. Before diving into troubleshooting, try these steps first:

1. **Verify your service is deployed and running:** a stopped service cannot respond to certificate validation challenges
2. **Clear your browser cache** or test in an incognito/private window
3. **Flush your local DNS cache:**
   - macOS: sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
   - Windows: ipconfig /flushdns
   - Linux: sudo resolvectl flush-caches (or sudo systemd-resolve --flush-caches on older systems)
4. **Test from a different device or network** to rule out local issues
5. **Wait at least an hour** after adding a domain before investigating

If the issue persists after these steps, continue with the troubleshooting sections below.

<Banner variant="warning">
**Avoid repeatedly deleting and re-adding your domain.** Let's Encrypt enforces strict rate limits (5 duplicate certificates per domain per week). If you hit this limit, you will be blocked from issuing a certificate for that domain for 7 days, even after fixing the underlying issue.
</Banner>

## Certificate stuck on "validating challenges"

If your domain shows that the Certificate Authority is validating challenges for an extended period, the certificate issuance process is not completing successfully.

### Why this happens

- DNS records have not propagated yet
- DNS records are incorrect
- CAA records are blocking Let's Encrypt
- DNSSEC is misconfigured
- Cloudflare proxy settings are interfering

### Solutions

#### Check DNS propagation

Verify your DNS records have propagated using a tool like dnschecker.org. Enter your domain and check that the CNAME record points to your Railway-provided value (e.g., abc123.up.railway.app).

**Note:** If you are using Cloudflare Proxy (orange cloud), DNS lookup tools will show Cloudflare IP addresses instead of the Railway CNAME. This is expected behavior. In this case, verify your DNS settings directly in your Cloudflare dashboard instead.

DNS changes can take up to 72 hours to propagate worldwide, though most propagate within a few hours.

<Collapse title="Using a root domain (apex domain)?">

If you're configuring a root domain (e.g., example.com without www), standard DNS does not allow CNAME records at the apex. Your DNS provider must support **CNAME Flattening**, **ALIAS records**, or **ANAME records** to work around this limitation.

Most modern DNS providers (Cloudflare, Namecheap, Vercel DNS, etc.) support this. If your provider does not, you have two options:
- Switch to a DNS provider that supports CNAME flattening
- Use a subdomain like www.example.com instead

</Collapse>

#### Check for caa records

CAA (Certificate Authority Authorization) records specify which certificate authorities are allowed to issue certificates for your domain. If you have CAA records that don't include Let's Encrypt, certificate issuance will fail.

To check for CAA records:

If you have CAA records, ensure Let's Encrypt is included:

If you don't have any CAA records, this is not your issue. The absence of CAA records allows any CA to issue certificates.

#### Check dnssec configuration

DNSSEC can interfere with certificate validation if misconfigured. To check DNSSEC status:

1. Visit dnsviz.net and enter your domain
2. Look for any errors or warnings in the DNSSEC chain

If DNSSEC is misconfigured, you'll need to either fix the configuration or disable DNSSEC through your domain registrar.

#### Cloudflare-specific issues

If you're using Cloudflare, ensure:

- The DNS record is proxied (orange cloud) for regular domains
- For wildcard domains, the _acme-challenge record must NOT be proxied (grey cloud)
- SSL/TLS mode is set to **Full** (not Full Strict)

**The Toggle Trick:** If your certificate is stuck on "Validating Challenges," try temporarily turning the Cloudflare proxy OFF (grey cloud), wait for Railway to issue the certificate (you'll see a green checkmark in Railway), then turn the proxy back ON (orange cloud). This removes Cloudflare from the validation path and allows Railway's Let's Encrypt challenge to reach the origin directly.

See the Cloudflare SSL Errors section for more details.

## Cloudflare SSL errors

When using Cloudflare with Railway, specific SSL configurations are required. **Use Full mode.** It encrypts all traffic while tolerating the temporary certificate states that occur during Railway's automatic certificate management.

### Err_too_many_redirects

This typically happens when Cloudflare's SSL mode doesn't match Railway's configuration.

**Solution:** Set Cloudflare SSL/TLS mode to **Full**.

If you have SSL mode set to "Flexible", Cloudflare sends unencrypted requests to Railway, but Railway redirects HTTP to HTTPS, causing an infinite redirect loop.

### Error 526: invalid SSL certificate

This error means Cloudflare cannot validate the SSL certificate on Railway's origin server.

**Solution:** Set your Cloudflare SSL/TLS mode to **Full** (not Full Strict).

1. Go to your domain in Cloudflare dashboard
2. Navigate to SSL/TLS > Overview
3. Select **Full**

<Banner variant="warning">
Do not use **Full (Strict)** mode with Railway. Strict mode requires the origin certificate to be issued by a publicly trusted CA and match the hostname exactly, which can fail during certificate renewal windows.
</Banner>

<Collapse title="Why Full mode instead of Full (Strict)?">

This is not a security compromise. Full mode still encrypts all traffic between Cloudflare and Railway.

The difference is that Strict mode requires the origin certificate to match the exact hostname requested. During certificate provisioning or renewal, Railway may temporarily serve its default *.up.railway.app certificate. Strict mode rejects this as a hostname mismatch, while Full mode accepts it since the traffic is still encrypted.

Since your DNS points directly to Railway's infrastructure, there is no man-in-the-middle risk.

</Collapse>

### Error 525: SSL handshake failed

This error indicates Cloudflare could not complete an SSL handshake with Railway.

**Possible causes:**
- Railway has not yet issued a certificate for your domain
- There's a temporary issue with certificate provisioning

**Solutions:**
1. Wait for certificate issuance to complete (check your domain status in Railway)
2. Ensure your domain's DNS is correctly configured
3. Try toggling proxy off and on in Cloudflare

### Wildcard domain certificate issues

For wildcard domains on Cloudflare:

1. The _acme-challenge CNAME record **must not be proxied** (use grey cloud / DNS only)
2. Enable Universal SSL in Cloudflare
3. For nested wildcards (e.g., *.subdomain.example.com), you need Cloudflare's Advanced Certificate Manager

## Connection issues for some users

If SSL works for most users but not others, the issue is likely on the user's end.

### Why this happens

- Outdated browsers or operating systems that don't support modern TLS
- Corporate firewalls or proxies interfering with connections
- ISP-level filtering or outdated DNS resolvers
- Antivirus software intercepting HTTPS connections

### How to diagnose

Ask affected users to:

1. Try a different browser
2. Try a different network (e.g., mobile data instead of WiFi)
3. Disable antivirus temporarily
4. Check if they're behind a corporate proxy

If the issue only affects users on a specific ISP or network, it's likely a network-level issue outside Railway's control.

### Testing from your side

You can test SSL connectivity using command-line tools:

## Certificate shows wrong domain

If your browser shows a certificate for *.up.railway.app instead of your custom domain, the certificate for your domain hasn't been issued yet.

### Solutions

1. **Check domain status in Railway:** ensure it shows as verified (green checkmark)
2. **Verify DNS configuration:** your CNAME should point to the Railway-provided value
3. **Wait for issuance:** if you just added the domain, wait up to an hour
4. **Check for conflicting records:** ensure you don't have both A and CNAME records for the same hostname

## Using the network diagnostics tool

If you're still having issues, Railway provides a Network Diagnostics tool that can help identify connectivity problems between your location and Railway's infrastructure.

Download and run the tool, then share the results with Railway support if needed.

## When to contact support

Contact Railway support if:

- Certificate issuance has been stuck for more than 72 hours
- You've verified DNS is correct and there are no CAA/DNSSEC issues
- The Network Diagnostics tool shows problems
- You're experiencing issues that this guide doesn't address

You can reach support through Central Station by creating a thread in the Questions topic.

## Code Examples

dig CAA yourdomain.com

yourdomain.com.  CAA  0 issue "letsencrypt.org"

# Test SSL connection
openssl s_client -connect yourdomain.com:443 -servername yourdomain.com

# Check certificate details
echo | openssl s_client -connect yourdomain.com:443 -servername yourdomain.com 2>/dev/null | openssl x509 -noout -dates


# Network diagnostics
Source: https://docs.railway.com/networking/troubleshooting/network-diagnostics

Troubleshoot network issues using Railway's network diagnostic tool

following tool to help us diagnose the problem.

<Image src="https://res.cloudinary.com/railway/image/upload/v1756932024/docs/205816ef-5cc5-4925-b807-f34c6ce09d95.png"
alt="Screenshot of NetDiag application"
layout="intrinsic"
width={642} height={670} quality={100} />

## Download

The latest version of the tool is available for macOS and Windows:

- **macOS**
- **Windows**

## Instructions

1. Open the application and click "Run Diagnostics":

<Image src="https://res.cloudinary.com/railway/image/upload/v1756932289/docs/step-share-diagnostics_tebnh5.png"
alt="NetDiag - Run diagnostics"
layout="intrinsic"
width={642} height={670} quality={100} />

2. Once the diagnostics are complete, click "Copy to Clipboard" or "Save to File":

<Image src="https://res.cloudinary.com/railway/image/upload/v1756932289/docs/step-save-output_vr98ug.png"
alt="NetDiag - Share output"
layout="intrinsic"
width={642} height={670} quality={100} />

3. Share the output with Railway Support

## Source Code

NetDiag is open source and available on GitHub.


# Application failed to respond
Source: https://docs.railway.com/networking/troubleshooting/application-failed-to-respond

Learn how to troubleshoot and fix the 'Application Failed to Respond' error.

alt="Screenshot of application failed to respond error"
layout="intrinsic"
width={1080} height={950}
quality={100} />

## What this error means

Seeing that your application failed to respond means that Railway's Edge Proxy cannot communicate with your application, causing your request to fail with a 502 (Bad Gateway) status code.

## Why this error can occur

There are a few reasons why this error can occur, the most common being that your application is not listening on the correct host or port.

Another common reason is that your target port is set to an incorrect value.

In some far less common cases this error can also occur if your application is under heavy load and is not able to respond to the incoming request.

## Possible solutions

The correct solution depends on the cause of the error.

### Target port set to the incorrect value

If your domain is using a target port, ensure that the target port for your public domain matches the port your application is listening on.

This setting can be found within your service settings.

<Image src="https://res.cloudinary.com/railway/image/upload/v1743470803/docs/custom-port_r8vhbx.png"
alt="Screenshot showing target ports on a domain"
layout="intrinsic"
width={1200}
height={999}
quality={100}
/>

In the screenshot above, the domain was previously incorrectly configured with port 3000, when the application was actually listening on port 8080.

### Application not listening on the correct host or port

Your web server should bind to the host 0.0.0.0 and listen on the port specified by the PORT environment variable, which Railway automatically injects into your application.

Start your application's server using:

- Host = 0.0.0.0
- Port = Value of the PORT environment variable provided by Railway.

**Below are some solution examples for common languages and frameworks.**

#### Node / Express

#### Node / Nest

#### Node / next

Next needs an additional flag to listen on PORT:

#### Python / gunicorn

gunicorn listens on 0.0.0.0 and the PORT environment variable by default:

#### Python / uvicorn

uvicorn needs additional configuration flags to listen on 0.0.0.0 and PORT:

#### Go / net/http

This example is for net/http in the Go standard library, but you can also apply this to other frameworks:

### Application under heavy load

If you think your application could be under heavy load, you can confirm this by checking the Metrics tab within your service panel.

For example, if you are running a Node.js application, and see that your vCPU usage has peaked at any point to around 1 vCPU, this is a good indication that your application is under heavy load given Node's single-threaded nature.

If this is the case, you can scale your application horizontally to handle more requests.

Horizontal scaling can easily be done by adding more instances to one or more regions.

## Code Examples

// Use PORT provided in environment or default to 3000
const port = process.env.PORT || 3000;

// Listen on `port` and 0.0.0.0
app.listen(port, "0.0.0.0", function () {
  // ...
});

// Use `PORT` provided in environment or default to 3000
const port = process.env.PORT || 3000;

// Listen on `port` and 0.0.0.0
async function bootstrap() {
  // ...
  await app.listen(port, "0.0.0.0");
}

next start --port ${PORT-3000}

gunicorn main:app

uvicorn main:app --host 0.0.0.0 --port $PORT

func main() {
  // ...
  // Use `PORT` provided in environment or default to 3000
  port := cmp.Or(os.Getenv("PORT"), 3000)

  log.Fatal(http.ListenAndServe((":" + port), handler))
  // ...
}


# 405 method not allowed
Source: https://docs.railway.com/networking/troubleshooting/405-method-not-allowed

Learn how to troubleshoot and fix the '405 Method Not Allowed' error.

This error is returned by your application when you attempt to make a POST request to your application, but the request is redirected to a GET request.

Depending on the application, this may result in your application returning either a 405 Method Not Allowed or a 404 Not Found status code.

Seemingly POST requests are being turned into GET requests.

## Why this error can occur

This occurs because your request was made using HTTP. Railway will attempt to redirect your insecure request with a 301 Moved Permanently status code.

When an HTTP client encounters a 301 Moved Permanently redirect, the client will follow the redirect. However, according to the <a href="https://www.rfc-editor.org/rfc/rfc7231#section-6.4.2" target="_blank">HTTP/1.1 specifications</a>, the client will typically change the request method from POST to GET when it follows the redirect to the new URL.

## Solution

Ensure you are explicitly using https:// when calling your Railway-hosted services.

For example, if you are using curl to test your application, you should use the following command:

Notice the https:// prefix.

This ensures that the request is made using HTTPS, avoiding the 405 Method Not Allowed error that your application would otherwise return.

## Code Examples

curl -X POST https://your-app.railway.app/api



# Observability
Source: https://docs.railway.com/observability

# Logs
Source: https://docs.railway.com/observability/logs

Learn how to view, filter, and search build, deployment, environment, and HTTP logs on Railway.

There are three ways to view logs in Railway.

- **Build/Deploy Panel** â Click on a deployment in the dashboard
- **Log Explorer** â Click on the Observability tab in the top navigation
- **CLI** â Run the railway logs command

## Build / deploy panel

Logs for a specific deployment can be viewed by clicking on the deployment in the service window, useful when debugging application failures.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1722993852/docs/CleanShot_2023-09-08_at_10.55.06_2x_co6ztr.png"
alt="deploy logs for a specific deployment"
layout="responsive"
width={1365} height={790} quality={80} />

Similarly, logs for a specific build can be viewed by clicking on the **Build Logs** tab once you have a deployment open.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1722993947/docs/build_logs_og7uec.png"
alt="deploy logs for a specific deployment"
layout="responsive"
width={1365} height={790} quality={80} />

## Log explorer

Logs for the entire environment can be viewed together by clicking the "Observability" button in the top navigation. The Log Explorer is useful for debugging more general problems that may span multiple services.

The log explorer also has additional features like selecting a date range or toggling the visibility of specific columns.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1694194133/docs/log-explorer_nrlong.png"
alt="Railway Log Explorer"
layout="responsive"
width={1166} height={650} quality={80} />

## Command line

Deployment logs can also be viewed from the command line to quickly check the current status of the latest deployment. Use railway logs to view them.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1694195563/docs/CleanShot_2023-09-08_at_10.52.12_2x_yv1d7f.png"
alt="Viewing logs using the command line interface"
layout="responsive"
width={1489} height={591} quality={80} />

## Filtering logs

Railway supports a custom filter syntax that can be used to query logs.

Filter syntax is available for all log types, but some log types have specific attributes.

### Filter syntax

- <keyword> or "key phrase" â Filter for a partial substring match
- @attribute:value â Filter by custom attribute (see structured logs below)
- @arrayAttribute[i]:value â Filter by an array element
- replica:<replica_id> â Filter by a specific replica's UUID

You can combine expressions with boolean operators AND, OR, and - (negation). Parentheses can be used for grouping.

#### Numeric comparisons

Numeric filtering uses comparison operators and ranges, and works for deployment logs with JSON logging. It's also supported for these HTTP log attributes:

- @totalDuration â Total request duration in milliseconds
- @responseTime â Time to first byte in milliseconds
- @upstreamRqDuration â Upstream request duration in milliseconds
- @httpStatus â HTTP status code
- @txBytes â Bytes transmitted (response size)
- @rxBytes â Bytes received (request size)

**Supported operators:**

- > â Greater than
- >= â Greater than or equal to
- < â Less than
- <= â Less than or equal to
- .. â Range (inclusive)

### Log type attributes

#### Environment logs

Environment logs allow you to query for logs from the environment they were emitted in. This means that you can search for logs emitted by all services in an environment at the same time, all in one central location.

In addition to the filters available for deployment logs, an additional filter is available for environment logs:

- @service:<service_id> â Filter by a specific service's UUID

#### HTTP logs

HTTP logs use the same filter syntax, but have a specific set of attributes for HTTP-specific data.

- @requestId:<request_id> â Filter by request ID
- @timestamp:<timestamp> â Filter by timestamp (Formatted in RFC3339)
- @method:<method> â Filter by method
- @path:<path> â Filter by path
- @host:<host> â Filter by host
- @httpStatus:<status_code> â Filter by HTTP status code
- @responseDetails:<details> â Filter by response details (Only populated when the application fails to respond)
- @clientUa:<user_agent> â Filter by a specific client's user agent
- @srcIp:<ip> â Filter by source IP (The client's IP address that made the request)
- @edgeRegion:<region> â Filter by edge region (The region of the edge node that handled the request)

### Examples

#### Deployment logs

Find logs that contain the word request.

Find logs that contain the substring POST /api.

Find logs with an error level.

Find logs with a warning level.

Find logs with an error level that contain specific text.

Find logs with a specific custom attribute.

Find logs with a specific array attribute.

Find tasks that take 10 minutes or more.

Find batches with more than 100 items.

Find retries between 1 and 3.

#### Environment logs

Filter out logs from the Postgres database service.

Filter logs from the Postgres database service and the Redis cache service.

Show only logs from the Postgres database and Redis cache services.

#### HTTP logs

Find logs for a specific path.

Find logs for a specific path that returned a 500 error.

Find logs for a specific path that returned a 500 or 501 error.

Find all non-200 responses.

Find all requests that originated from or around Europe.

Find all requests that originated from a specific IP address.

Find slow responses taking more than 500ms.

Find responses taking 1 second or more.

Find fast responses under 100ms.

Find responses between 100-500ms.

Find all error responses (4xx and 5xx).

Find only server errors (5xx).

Find all successful responses (1xx, 2xx, 3xx).

Find large responses over 1MB.

Find requests with body larger than 5KB.

Combine filters to find slow requests that errored.

Find slow, large responses.

## View in context

When searching for logs, it is often useful to see surrounding logs. To view a log in context:
right-click any log, then select the "View in Context" option from the dropdown menu.

## Structured logs

Structured logs are logs emitted in a structured JSON format, useful if you want
to attach custom metadata to logs or preserve multi-line logs like stack traces.

Structured logs are best generated with a library for your language. For example, the default <a href="https://github.com/winstonjs/winston" target="_blank">Winston</a> JSON format emits logs in the correct structure by default.

Logs with a level field will be coloured accordingly in the log explorer.

Logs emitted to stderr will be converted to level.error and coloured red.

### Examples

Here are a few examples of structured logs.

**Note:** The entire JSON log must be emitted on a single line to be parsed correctly.

### Normalization strategy

In order to ensure a consistent query format across Railway services, incoming logs are normalized to the above format automatically.

- Non-structured logs are converted to {"message":"...","level":"..."}

- log.msg converted to log.message

- log.level converted to log.severity

- Logs from stderr are converted to level.error

- Logs from stdout are converted to level.info

- Levels are lowercased and matched to the closest of debug, info, warn, error

## Log retention

Depending on your plan, logs are retained for a certain amount of time.

| Plan          | Retention\*   |
| ------------- | ------------- |
| Hobby / Trial | 7 days        |
| Pro           | 30 days       |
| Enterprise    | Up to 90 days |

_\* Upgrading plans will immediately restore logs that were previously outside of the retention period._

## Logging throughput

To maintain quality of service for all users, Railway enforces a logging rate limit of **500 log lines per second per replica** across all plans. When this limit is exceeded, additional logs are dropped and you'll see a warning message like this:

If you encounter this limit, here are some strategies to reduce your logging volume:

- Reduce log verbosity in production
- Use structured logging with minimal formatting (e.g., minified JSON instead of pretty-printed objects)
- Implement log sampling for high-frequency events
- Conditionally disable verbose logging based on the environment
- Combine multiple related log entries into single messages

## Troubleshooting

Having issues with logs? Check out the Troubleshooting guide or reach out on the <a href="https://discord.gg/railway" target="_blank">Railway Discord</a>.

## Code Examples

request

"POST /api"

@level:error

@level:warn

@level:error AND "failed to send batch"

@customAttribute:value

@arrayAttribute[i]:value

@task_duration:>=600

@batch_size:>100

@retries:1..3

-@service:<postgres_service_id>

-@service:<postgres_service_id> AND -@service:<redis_service_id>

@service:<postgres_service_id> OR @service:<redis_service_id>

@path:/api/v1/users

@path:/api/v1/users AND @httpStatus:500

@path:/api/v1/users AND (@httpStatus:500 OR @httpStatus:501)

-@httpStatus:200

@edgeRegion:europe-west4-drams3a

@srcIp:66.33.22.11

@responseTime:>500

@responseTime:>=1000

@responseTime:<100

@responseTime:100..500

@httpStatus:>=400

@httpStatus:500..599

@httpStatus:<400

@txBytes:>1000000

@rxBytes:>5000

@totalDuration:>5000 @httpStatus:>=500

@responseTime:>1000 @txBytes:>100000

console.log(
  JSON.stringify({
    message: "A minimal structured log", // (required) The content of the log
    level: "info", // Severity of the log (debug, info, warn, error)
    customAttribute: "value", // Custom attributes (query via @name:value)
  }),
);

{ "level": "info", "message": "A minimal structured log" }

{ "level": "error", "message": "Something bad happened" }

{ "level": "info", "message": "New purchase!", "productId": 123, "userId": 456 }

{
  "level": "info",
  "message": "User roles updated",
  "roles": ["editor", "viewer"],
  "userId": 123
}

Railway rate limit of 500 logs/sec reached for replica, update your application to reduce the logging rate. Messages dropped: 50


# Metrics
Source: https://docs.railway.com/observability/metrics

Discover resource usage for your services on Railway via the Metrics tab.



## How it works

For each service, Railway captures metric data. These metrics are then made available in graphs within a service's panel, under the metrics tab.

## Accessing service metrics

Access a service's metrics by clicking on a service in the project canvas, and going to the "Metrics" tab.

<Image src="https://res.cloudinary.com/railway/image/upload/v1758559063/docs/metrics-sum_tvdwlc.png"
alt="Screenshot of Metrics Page"
layout="intrinsic"
width={1576} height={1100} quality={80} />

## Provided metrics

The following metrics are provided:

- **CPU** - Processor usage
- **Memory** - RAM consumption
- **Disk Usage** - Storage utilization
- **Network** - Inbound and outbound traffic

## Understanding the metrics graphs

Graphs include dotted lines to indicate when new deployments began. Up to 30 days of data is available for each project.

<Image src="https://res.cloudinary.com/railway/image/upload/v1645223703/docs/usage-commit_fkvbqj.png"
alt="Screenshot of Metric Timeseries Commit Information"
layout="responsive"
width={904} height={726} quality={80} />

Projects maintain a continuous time-series for all deployments within a service, not just the latest one. Deployments appear on the graph so users can see which commit may have caused a spike in resources.

## Metrics with multiple replicas

When a service runs multiple replicas, you can view metrics in two ways: **Sum** or **Replica**.

_Note: Public network traffic metrics are only available in the Sum view._

### Sum view

<Image src="https://res.cloudinary.com/railway/image/upload/v1758559063/docs/metrics-sum_tvdwlc.png"
alt="Viewing the sum of all replica metrics"
layout="intrinsic"
width={1576} height={1100} quality={80} />

In **Sum** view, metrics from all replicas are combined. For example, if you have two replicas using 100 MB of memory each, the metrics tab will show 200 MB.

### Replica view

<Image src="https://res.cloudinary.com/railway/image/upload/v1758559063/docs/metrics-per-replica_skc17b.png"
alt="Viewing metrics of individual replicas"
layout="intrinsic"
width={1576} height={1100} quality={80} />

In **Replica** view, you can see metrics for each replica individually. This is useful for diagnosing issues with specific replicas or spotting if some regions are under- or overutilized.

The total from all replicas may differ slightly from the Sum view due to rounding or overlapping instances during zero-downtime deployments.

## Troubleshooting

Having issues understanding your metrics? Check out the Troubleshooting guide or reach out on the <a href="https://discord.gg/railway" target="_blank">Railway Discord</a>.


# Webhooks
Source: https://docs.railway.com/observability/webhooks

Learn how to set up webhooks on Railway to receive real-time updates for deployments and events.

<Image src="https://res.cloudinary.com/railway/image/upload/v1763768800/new-webhooks_lhw6p2.png"
alt="New Webhook"
layout="responsive"
width={821} height={485} quality={80} />

## Setup a webhook

Complete the following steps to setup a webhook:

1. Open an existing Project on Railway.
1. Click on the Settings button in the top right-hand corner.
1. Navigate to the Webhooks tab.
1. Input your desired webhook URL.
1. Optional: specify which events to receive notifications for.
1. Click Save Webhook.

The URL you provide will receive a webhook payload when any service's deployment status changes or an alert is triggered. This will be executed across all environments in the project.

## Platform events

Webhooks can be used to receive notifications for a variety of events on the platform:

- **Deployment status changes** - Available deployment states can be found in the Deployments reference.
- **Volume usage alerts** - Notifications when volumes approach capacity.
- **CPU/RAM monitor alerts** - Notifications when resource usage exceeds thresholds.

## Webhook payload

When an event occurs, Railway sends a JSON payload to your configured webhook URL.

### Example payload

## Testing webhooks

The Test Webhook button will send a test payload to the specified webhook URL.

Note: For security reasons, test webhooks are sent from the frontend client, which may result in Cross-Origin Resource Sharing (CORS) restrictions. This typically presents as a delivery failure when using the test webhook functionality.

## Muxers: provider-specific webhooks

For certain webhook URLs, Railway will automatically transform the payload to match the destination (we call these Muxers). This makes it easy to use webhooks without having to write your own middleware to format the request body.

Currently supported providers:

- Discord
- Slack

### Setting up a webhook for discord

Discord supports integrating directly with webhooks. To enable this on a server you will need to be an admin or otherwise have the appropriate permissions.

1. On Discord, open the settings for a server text channel. This menu can be accessed via the cogwheel/gear icon where the channel is listed on the server.
2. Click on the integrations tab.
3. Click on the webhooks option.
4. You will see an option to create a new webhook, click this button and fill out your preferred bot name and channel.
5. Once created, you will have the option to copy the new webhook URL. Copy that URL.
6. Back in Railway, open the project you wish to integrate with.
7. Click on the project's deployments menu.
8. Navigate to the settings tab.
9. Input the copied webhook URL into the input under "Build and Deploy Webhooks".
10. Click the checkmark to the right of the input to save.

At this point, the Discord Muxer will identify the URL and change the payload to accommodate the Discord integration. You can see this if you expand the payload preview panel.

You are now done! When your project deploys again, that Discord channel will get updates on the deployment!

### Setting up a webhook for slack

Slack supports integrating directly with webhooks.

1. Enable incoming webhooks for your Slack instance (Tutorial <a href="https://api.slack.com/messaging/webhooks#enable_webhooks" target="_blank">here</a>)
1. Generate a hooks.slack.com webhook URL for your channel (Tutorial <a href="https://api.slack.com/messaging/webhooks#create_a_webhook" target="_blank">here</a>)
1. Open up Railway, navigate to your project's Webhook tab.
1. Paste the url from slack

<Image
src="https://res.cloudinary.com/railway/image/upload/v1737947755/docs/webhooks/wo4tuyv9dy7gjgiq2j7j.png"
alt="Slack Webhook"
layout="responsive"
width={1466} height={810} quality={80} />

## Troubleshooting

Having issues with webhooks? Check out the Troubleshooting guide or reach out on the <a href="https://discord.gg/railway" target="_blank">Railway Discord</a>.

## Code Examples

{
  "type": "Deployment.failed",
  "details": {
    "id": "8107edff-4b8e-44fc-b43a-04566e847a2a",
    "source": "GitHub",
    "status": "SUCCESS",
    "branch": "...",
    "commitHash": "...",
    "commitAuthor": "...",
    "commitMessage": "...",
  },
  "resource": {
    "workspace": { "id": "<workspace id>", "name": "<workspace name>" },
    "project": { "id": "<project id>", "name": "<project name>" },
    "environment": { "id": "<environment id>", "name": "<environment name>", "isEphemeral": false },
    "service": { "id": "<service id>", "name": "<service name>" },
    "deployment": { "id": "<deployment id>" }
  },
  "severity": "WARNING",
  "timestamp": "2025-11-21T23:48:42.311Z"
}



# Access
Source: https://docs.railway.com/access

# Accounts
Source: https://docs.railway.com/access/accounts

Learn about Railway Accounts

Users are only allowed one account per person. This is enforced through email, GitHub, and payment method verification.

## Account settings

<Image src="https://res.cloudinary.com/railway/image/upload/v1743471483/docs/account-settings_najujk.png"
alt="Screenshot of Account Navigation"
layout="responsive"
width={1200} height={857} quality={80} />

The account settings page is accessible by clicking the profile photo in the top right and selecting <a href="https://railway.com/account" target="_blank">Account Settings</a>.

### Account information

Accounts can change their display name, profile photo, and account email under <a href="https://railway.com/account" target="_blank">Account Settings</a>.

### Deleting an account

Selecting "Delete Account" at the bottom of the <a href="https://railway.com/account" target="_blank">Account Settings</a> page will delete an account. All data related to the account will be deleted.

After a successful confirmation, Railway deletes all account information, project data, and removes the account from all email lists.

We aim to be compliant with EU GDPRâs data removal provisions.

## Account security

<Image src="https://res.cloudinary.com/railway/image/upload/v1631917786/docs/sessions_qo0lhw.png"
alt="Screenshot of Sessions Page"
layout="responsive"
width={1162} height={587} quality={80} />

Railway is committed to you and your project's security. We provide a variety of methods to help keep users' peace of mind.

### Two-factor authentication

Two-factor authentication can be enabled under the Account Security page. Most TOTP applications are supported.

After scanning the provided QR code and entering the code for the initial pairing of the application, 2FA will require additional verification for login and destructive actions.

### Account sessions

Users can view all active browser and CLI sessions on the <a href="https://railway.com/account/security" target="_blank">account security page</a>. Revoking a session will immediately log that device out.

## Referrals

<Image src="https://res.cloudinary.com/railway/image/upload/v1631917786/docs/referrals_cash_ashj73.png"
alt="Screenshot of Referrals Page"
layout="intrinsic"
width={1784} height={1104} quality={80} />

Every account has an editable referral link. Users can copy and share their personal referral link to earn cash or credits.

Any user who is referred gets $20 in Railway credits, equivalent to a free month on the Pro tier.

Upon every invoice a referral pays, the user who referred them receives 15% commission on that revenue.

Users can view their referral invite status on the <a href="https://railway.com/account/referrals" target="_blank">referrals page</a>, and their total earnings on the <a href="https://railway.com/account/earnings" target="_blank">earnings page</a>.

## Billing

Accounts are billed monthly. Resources used by deleted projects up until the time of deletion are still counted towards the total bill.

Railway may collect applicable sales tax and VAT on your account based on your billing location and local tax requirements, where and when applicable. To ensure accurate tax assessment, Workspace Admins must verify that their billing information, including Billing Address, Organization Name, and Tax ID, is accurate. Organization Name and Tax ID are not required when using Railway for personal use.

Users can manage their billing information as well as view historical payments on the <a href="https://railway.com/workspace/billing" target="_blank">billing page</a>.

## Link discord account

Within Account settings, link a Discord account with a Railway account to gain access to additional features on the <a href="https://discord.gg/railway" target="_blank">Railway Discord server</a>.

If the Discord user has not joined the Railway Discord server, linking the account will automatically invite the user to the server.

### Discord support

Discord users can access the <a href="https://discord.gg/railway" target="_blank">Railway Discord server</a> to get help from the Railway team and other users.

### Priority boarding enrollment

For the most adventurous, we offer a beta program called Priority Boarding. You can join by flipping the "Priority Boarding" switch on the <a href="https://railway.com/account/feature-flags" target="_blank">Feature Flags page</a>. To learn more, visit Priority Boarding.


# Two-factor enforcement
Source: https://docs.railway.com/access/two-factor-enforcement

Learn how workspace admins can require two-factor authentication for all workspace members.

2FA Enforcement is available on the Pro plan and above.
</Banner>

Two-Factor Authentication (2FA) Enforcement allows workspace admins to require all members to have 2FA enabled on their account before accessing the workspace.

## Enabling 2FA enforcement

<Image src="https://res.cloudinary.com/railway/image/upload/v1723752559/docs/reference/2fa/enable-2fa-enforcement.png"
alt="Screenshot of 2FA Enforcement toggle in workspace People settings"
layout="responsive"
width={1610} height={398} quality={80} />

To enable 2FA enforcement for your workspace:

1. Navigate to your workspace's <a href="https://railway.com/workspace/people" target="_blank">People settings</a>.
2. Toggle the **Require 2FA** option.

You must be a workspace admin with 2FA already enabled on your account to configure this setting.

Once enabled, enforcement takes effect immediately. Members who haven't set up 2FA will be prompted to configure it before they can access the workspace.

## Behavior

<Image src="https://res.cloudinary.com/railway/image/upload/v1723752559/docs/reference/2fa/2fa-enforcement-modal.png"
alt="Screenshot of 2FA setup prompt when accessing a workspace with 2FA enforcement"
layout="responsive"
width={836} height={744} quality={80} />

When 2FA enforcement is enabled:

- Existing members without 2FA are prompted to set it up before accessing the workspace.
- Members can still be invited to the workspace. They can accept the invite, but must enable 2FA before accessing workspace resources.
- Users joining via Trusted Domains are added to the workspace, but must enable 2FA before accessing workspace resources.
- New members cannot view or interact with workspace projects until 2FA is configured.

## Access methods

- **Dashboard and CLI**: All workspace members must have 2FA enabled to access the workspace through the Railway dashboard or CLI.
- **API Tokens**: Access token-based access (such as project tokens or workspace tokens used for CI/CD pipelines and automated deployments) remains valid without 2FA. This ensures your automated workflows continue to function without interruption.

## Disabling 2FA enforcement

Workspace admins can disable 2FA enforcement at any time through the workspace's People settings. Once disabled, members are no longer required to have 2FA enabled to access the workspace.


# Multi-factor authentication
Source: https://docs.railway.com/access/multi-factor-authentication

Secure your Railway account with multi-factor authentication using authenticator apps or passkeys.

Railway supports two MFA methods:
- **Authenticator App** - Use a time-based one-time password (TOTP) from an authenticator app
- **Passkeys** - Use your device's built-in authentication (fingerprint, face recognition, or PIN)

## Authenticator app

Use an authenticator app like Google Authenticator, Authy, or 1Password to generate time-based verification codes.

### Setup

1. Go to your Account Security Settings page
2. Click the **Set up two-factor authentication** button
3. Scan the QR code with your authenticator app
4. Enter the verification code from your authenticator app to confirm setup

Once enabled, you'll need to enter a code from your authenticator app each time you sign in. 

### Recovery codes

After setting up two-factor authentication, you'll receive a set of recovery codes. These codes serve as an alternative login method if you lose access to your authenticator app or are unable to receive a verification code.

<Banner variant="warning">
**Treat recovery codes like passwords.** Store them in a safe place. You'll need them if you lose access to your authenticator app.
</Banner>

Each recovery code can only be used once. If you've used most of your codes, you can generate a new set from your account settings.

## Passkeys

Passkeys use your device's built-in authentication (such as fingerprint, face recognition, or PIN) as a second verification step.

### Setup

1. Go to your Account Security Settings page
2. Click the **Add Passkey** button
3. Follow your device's prompts to register the passkey

### Benefits

- Phishing-resistant - Passkeys are bound to specific websites and can't be used on fake sites
- No codes to enter - Authentication happens automatically with your device
- Cross-device support - Many passkeys can be synced across your devices via iCloud Keychain, Google Password Manager, or similar services

## Managing MFA

You can manage your MFA settings at any time from your Account Security Settings page:

- View and regenerate recovery codes
- Add or remove passkeys
- Disable two-factor authentication (not recommended)

## Team enforcement

Team administrators can require all team members to have MFA enabled. See Two-Factor Enforcement for details.



# Integrations
Source: https://docs.railway.com/integrations

# Quickstart
Source: https://docs.railway.com/integrations/oauth/quickstart

Get started with Login with Railway in 5 steps.



## 1. Create an OAuth app

Navigate to your workspace settings â **Developer** â **New OAuth App**, and enter the app name and one or more redirect URIs. The redirect URIs you configure must exactly match what your application sends in authorization requests.

<Banner variant="info">
For native apps, use http://127.0.0.1:3000/callback (not localhost), or a custom URL scheme like myapp://callback.
</Banner>

After creating the app, copy the client ID and client secret. The secret is only shown once.

## 2. Redirect to authorization

When a user wants to sign in, redirect their browser to the authorization endpoint:

- response_type: Must be code
- client_id: Your OAuth app's client ID
- redirect_uri: Must exactly match a registered URI
- scope: Space-separated permissions; openid is required
- state: Random string for CSRF protection; verify it matches when redirected back

For additional security, add PKCE parameters. While optional for web apps, PKCE is mandatory for native apps. See Creating an App for details.

## 3. Exchange Code for tokens

After the user approves, they are redirected to your redirect_uri with a code parameter. Exchange it for tokens using Basic authentication:

Response:

The access_token authenticates API requests and expires in one hour. The id_token is a signed JWT to verify the user's identity.

## 4. Get user info

Retrieve the authenticated user's profile:

- The sub claim is the user's ID. You can use this to associate the Railway account with a user in your application.

## 5. Make API requests

Use the access token with the Public API:

## Next steps

- Login & Tokens: Token lifecycle and refresh tokens for long-lived access
- Scopes & User Consent: Available scopes and permissions
- Fetching Workspaces or Projects: Query resources users granted access to

## Code Examples

https://backboard.railway.com/oauth/auth
  ?response_type=code
  &client_id=YOUR_CLIENT_ID
  &redirect_uri=https://yourapp.com/callback
  &scope=openid+email+profile
  &state=RANDOM_STATE_VALUE

curl -X POST https://backboard.railway.com/oauth/token \
  -u "YOUR_CLIENT_ID:YOUR_CLIENT_SECRET" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  -d "code=AUTHORIZATION_CODE" \
  -d "redirect_uri=https://yourapp.com/callback"

{
  "access_token": "...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "id_token": "ey...",
  "scope": "openid email profile"
}

curl https://backboard.railway.com/oauth/me \
  -H "Authorization: Bearer ACCESS_TOKEN"

{
  "sub": "user_abc123",
  "email": "user@example.com",
  "name": "Jane Developer",
  "picture": "https://avatars.githubusercontent.com/u/12345"
}

curl https://backboard.railway.com/graphql/v2 \
  -H "Authorization: Bearer ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "query { me { name email } }"}'

{
  "data": {
    "me": {
      "name": "Jane",
      "email": "jane.doe@example.tld"
    }
  }
}


# Creating an app
Source: https://docs.railway.com/integrations/oauth/creating-an-app

Create and configure OAuth applications for Login with Railway.



## App types

Two types of OAuth applications are supported:

| Type | Client Secret | PKCE | Auth Method |
|------|---------------|------|-------------|
| Web (Confidential) | Required | Recommended | client_secret_basic or client_secret_post |
| Native (Public) | None | Required | none |

### Web applications

Web applications are confidential clients. They run on servers you control, where a client secret can be stored securely.

Even though web apps have a client secret, implementing PKCE is strongly recommended. PKCE protects against authorization code interception if an attacker manages to observe the redirect.

### Native applications

Native applications include mobile apps, desktop applications, command-line tools, and single-page applications running entirely in the browser. These are public clients because any secrets embedded in them could be extracted by users or attackers. You cannot trust that a secret will remain confidential.

Native apps authenticate using PKCE exclusively. Do not send a client secret, otherwise the token request will fail.

## Creating an app

To register a new OAuth app, go to your workspace settings, navigate to **Developer**, and click **New OAuth App**. Enter a name that users will recognize on the consent screen, add your redirect URI(s), and select the appropriate app type.

For web applications, a client secret is generated after creation. Copy this immediately. It's displayed only once. Store it securely in your application's configuration, such as an environment variable or secrets manager. Never commit it to version control.

## Redirect URIs

Redirect URIs specify where users are sent after they authorize (or deny) your application. You can register multiple URIs to support different environments. For example, http://localhost:3000/callback for local development and https://yourapp.com/callback for production.

When initiating authorization, the redirect_uri parameter must exactly match one of your registered URIs. This includes the scheme, host, port, and path. If they don't match, the authorization request fails with an invalid_redirect_uri error.

## PKCE (proof key for Code exchange)

PKCE adds a layer of protection to the authorization code flow. Without PKCE, an attacker who intercepts an authorization code could potentially exchange it for tokens. With PKCE, they would also need the code verifier: a secret that never travels through the redirect.

Add the code challenge to your authorization request:

When exchanging the authorization code for tokens, include the original code verifier:

## Dynamic client registration

OAuth 2.0 Dynamic Client Registration is supported, allowing applications to register OAuth clients programmatically rather than through the UI. This is useful for development tools that need to bootstrap OAuth configuration.

### Endpoint

Dynamic registration requests are subject to rate limits to prevent abuse.

### Managing dynamic clients

Clients created through dynamic registration are managed exclusively through the Dynamic Client Registration Management API. They don't appear in the workspace settings UI. When you register a client, the response includes a registration access token. Use this token to update or delete the client later.

Store the registration access token securely alongside your client credentials. Without it, you cannot modify or delete the dynamically registered client.

## Code Examples

https://backboard.railway.com/oauth/auth
  ?response_type=code
  &client_id=YOUR_CLIENT_ID
  &redirect_uri=https://yourapp.com/callback
  &scope=openid
  &code_challenge=CODE_CHALLENGE
  &code_challenge_method=S256

curl -X POST https://backboard.railway.com/oauth/token \
  -u "YOUR_CLIENT_ID:YOUR_CLIENT_SECRET" \
  -d "grant_type=authorization_code" \
  -d "code=AUTHORIZATION_CODE" \
  -d "redirect_uri=https://yourapp.com/callback" \
  -d "code_verifier=CODE_VERIFIER"

POST https://backboard.railway.com/oauth/register


# Login & tokens
Source: https://docs.railway.com/integrations/oauth/login-and-tokens

Understand the OAuth authorization flow and token lifecycle.

<Banner variant="info">
We recommend using an OAuth 2.0 / OpenID Connect library for your language or framework rather than implementing the flow manually.
</Banner>

## Initiating login

Redirect the user to the authorization endpoint:

| Parameter | Required | Description |
|-----------|----------|-------------|
| response_type | Yes | Must be code |
| client_id | Yes | Your OAuth app's client ID |
| redirect_uri | Yes | Must exactly match a registered URI |
| scope | Yes | Space-separated scopes (openid required) |
| state | Recommended | Random string for CSRF protection |
| code_challenge | Native Apps: Required, Web Apps: Recommended | PKCE challenge |
| code_challenge_method | With PKCE | Must be S256 |
| prompt | No | Set to consent to force consent screen |

### Authorization response

If the user approves your application, they are redirected to your redirect URI with an authorization code:

The code is short-lived and single-use. Exchange it for tokens immediately. If the user denies access, the redirect includes an error parameter instead.

Response:

## Access tokens

Access tokens authenticate your application's requests to Railway's API. When you call the Public API, include the access token in the Authorization header:

## Refresh tokens

Access tokens expire after one hour. For applications that need longer-lived access (background jobs, scheduled tasks, or simply avoiding frequent re-authentication) refresh tokens provide a way to obtain new access tokens without user interaction.

### Obtaining refresh tokens

To receive a refresh token, your authorization request must include both the offline_access scope and the prompt=consent parameter:

The prompt=consent ensures the user sees the consent screen, which is required for granting offline access. Without it, returning users might skip consent through automatic approval, and no refresh token would be issued.

Response:

### Refreshing tokens

When your access token expires (or is about to), exchange the refresh token for a new access token:

Refresh tokens are rotated for security. The response includes a refresh_token field that may initially contain the same value, but will eventually return a new token. Always store and use the refresh token from the most recent response. **Using an old, rotated token will fail, and the user would need to re-authenticate.** The new refresh token has a fresh one-year lifetime from the time of issuance.

<Banner variant="info">
Each user authorization can have a maximum of 100 refresh tokens. If you exceed this limit, the oldest tokens are revoked automatically.
</Banner>

## ID tokens

ID tokens are JSON Web Tokens (JWTs). Unlike access tokens, which are opaque and meant for API authorization, ID tokens are designed to be parsed and validated by your application to confirm who authenticated.

### Claims

The claims are not present in the ID token, but can be obtained by calling the /oauth/me endpoint.

| Claim | Scope Required | Description |
|-------|----------------|-------------|
| sub | openid | User's unique identifier |
| email | email | User's email address |
| name | profile | User's display name |
| picture | profile | URL to user's avatar |

The sub claim is always present and is stable for a given user. Use it to identify returning users in your application.

## Pushed authorization requests (PAR)

Pushed Authorization Requests (PAR) are supported. This keeps authorization details out of browser history. Instead of passing all parameters in the browser redirect, you first POST them to the PAR endpoint:

It returns a request_uri that references your stored parameters. Use this URI in the authorization redirect instead of the full parameter set.

## Code Examples

GET https://backboard.railway.com/oauth/auth

https://yourapp.com/callback?code=AUTHORIZATION_CODE&state=abc123&iss=https%3A%2F%2Fbackboard.railway.com

curl -X POST https://backboard.railway.com/oauth/token \
  -u "YOUR_CLIENT_ID:YOUR_CLIENT_SECRET" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  -d "code=AUTHORIZATION_CODE" \
  -d "redirect_uri=https://yourapp.com/callback"

{
  "access_token": "...",
  "expires_in": 3600,
  "id_token": "...",
  "scope": "openid email profile",
  "token_type": "Bearer"
}

curl -X POST https://backboard.railway.com/graphql/v2 \
  -H "Authorization: Bearer ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "query { me { name email } }"}'

https://backboard.railway.com/oauth/auth
  ?response_type=code
  &client_id=YOUR_CLIENT_ID
  &redirect_uri=https://yourapp.com/callback
  &scope=openid+offline_access
  &prompt=consent

{
  "access_token": "...",
  "expires_in": 3600,
  "id_token": "...",
  "refresh_token": "...",
  "scope": "openid email profile offline_access",
  "token_type": "Bearer"
}

curl -X POST https://backboard.railway.com/oauth/token \
  -u "YOUR_CLIENT_ID:YOUR_CLIENT_SECRET" \
  -d "grant_type=refresh_token" \
  -d "refresh_token=REFRESH_TOKEN"

{
  "access_token": "...",
  "expires_in": 3600,
  "id_token": "...",
  "refresh_token": "...",
  "scope": "openid email profile offline_access",
  "token_type": "Bearer"
}

curl https://backboard.railway.com/oauth/me \
  -H "Authorization: Bearer ACCESS_TOKEN"

{
  "sub": "user_abc123",
  "email": "user@example.com",
  "name": "Jane Developer",
  "picture": "https://avatars.githubusercontent.com/u/12345"
}

curl -X POST https://backboard.railway.com/oauth/request \
  -u "YOUR_CLIENT_ID:YOUR_CLIENT_SECRET" \
  -d "redirect_uri=https://yourapp.com/callback" \
  -d "scope=openid email profile" \
  -d "response_type=code"

https://backboard.railway.com/oauth/auth
  ?client_id=YOUR_CLIENT_ID
  &request_uri=urn:ietf:params:oauth:request_uri:abc123


# Scopes & user consent
Source: https://docs.railway.com/integrations/oauth/scopes-and-user-consent

Configure OAuth scopes to request appropriate permissions from users.



## Available scopes

| Scope | Description |
|-------|-------------|
| openid | Required for all requests. |
| email | Access user's email address in claims |
| profile | Access user's name and picture in claims |
| offline_access | Receive refresh tokens (requires prompt=consent) |
| workspace:viewer | Viewer access to user-selected workspaces |
| workspace:member | Member access to user-selected workspaces |
| workspace:admin | Admin access to user-selected workspaces |
| project:viewer | Viewer access to user-selected projects |
| project:member | Member access to user-selected projects |

The offline_access scope grants refresh tokens, but only when combined with prompt=consent in the authorization request. Refresh tokens allow your application to obtain new access tokens after the original expires, enabling long-running access without requiring users to re-authenticate.

Workspace and project scopes grant access to Railway resources. These are selective: the user chooses which specific workspaces or projects to share during consent. Your application only receives access to the resources they select, not their entire account.

<Banner variant="info">
The scope you request sets the maximum access level, but the user's actual role may be lower. For example, if your app requests workspace:admin but the user is only a member, the token will have member-level access.
</Banner>

## Claims

Claims are attributes about the user which can be accessed through the /oauth/me endpoint. Which claims you receive depends on the scopes the user approved:

| Claim | Required Scope |
|-------|----------------|
| sub | openid |
| email | email |
| name | profile |
| picture | profile |

The sub claim is the user's unique, stable identifier within Railway. Use this to associate their Railway account with records in your application's database.

## Consent screen

When a user authorizes your application, a consent screen is displayed showing your app's name and the permissions you're requesting. This transparency lets users make informed decisions about what access to grant.

### Workspace and project selection

When your app requests workspace or project scopes, the consent screen allows users to select which workspaces or projects they want to grant access to.

- For workspace scopes (workspace:viewer, workspace:member, workspace:admin), users pick from their available workspaces. Your application receives access only to the workspaces they select.
- For project scopes (project:viewer, project:member), users pick from projects across all their workspaces.

### Automatic consent

If a user has previously authorized your application with the same or broader scopes, the consent screen may be skipped and users are redirected immediately.

However, if you request workspace or project scopes, users might want to change which resources they share, but the consent screen may be skipped.

To always show the consent screen, add prompt=consent to your authorization request.

## Role permissions

Workspace and project scopes map to Workspace Roles and Project Member Roles. The access your application receives through these scopes matches what a user with that role could do through the Railway dashboard or API.

## Missing a scope?

If the available scopes don't cover your use case, we'd love to hear about it. Share your feedback on <a href="https://station.railway.com" target="_blank">Central Station</a> so we can learn about what you're building.


# Fetching workspaces or projects
Source: https://docs.railway.com/integrations/oauth/fetching-workspaces-or-projects

Query workspaces and projects the user has granted access to.



## Fetching workspaces

Workspace queries return the workspaces a user granted access to when authorizing your application. This requires that the user approved a workspace scope (workspace:viewer, workspace:member, or workspace:admin) and that your authorization request included the email and profile scopes alongside it.

**Query:**

This query returns the ID and name of each workspace. You can extend it to request additional fields depending on what your application needs. Consult the GraphQL schema for available fields.

**Example Request:**

**Response:**

The response includes only the workspaces the user selected during consent.

## Fetching projects

Project queries work similarly but use the externalWorkspaces field, which returns workspaces along with the specific projects the user granted access to. This requires a project scope (project:viewer or project:member) in the original authorization request.

Unlike workspace scopes, project scopes let users share individual projects without granting access to the entire workspace.

**Query:**

**Example Request:**

**Response:**

## Code Examples

query {
  me {
    workspaces {
      id
      name
    }
  }
}

curl -X POST https://backboard.railway.com/graphql/v2 \
  -H "Authorization: Bearer ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "query { me { workspaces { id name } } }"}'

{
  "data": {
    "me": {
      "workspaces": [
        {
          "id": "...",
          "name": "My Workspace"
        },
        {
          "id": "...",
          "name": "ACME Inc."
        }
      ]
    }
  }
}

query {
  externalWorkspaces {
    id
    name
    projects {
      id
      name
    }
  }
}

curl -X POST https://backboard.railway.com/graphql/v2 \
  -H "Authorization: Bearer ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "query { externalWorkspaces { id name projects { id name } } }"}'

{
  "data": {
    "externalWorkspaces": [
      {
        "id": "...",
        "name": "My Workspace",
        "projects": [
          {
            "id": "...",
            "name": "mywebsite.com"
          },
          {
            "id": "...",
            "name": "workflow automations"
          }
        ]
      }
    ]
  }
}


# Managing an app
Source: https://docs.railway.com/integrations/oauth/managing-an-app

Configure and manage your OAuth applications.



## Accessing app settings

To manage an OAuth app, go to your workspace settings and navigate to **Developer**.

- See and copy the client ID
- Update the application name
- Update the description
- Update the redirect URIs
- Update the logo
- Create or revoke client secrets

The settings page shows your app's client ID, which you can copy for use in your application. You can also edit the app's name (shown to users on the consent screen) and manage the redirect URIs where users are sent after authorization.

## Client secrets

Client secrets authenticate your application during the token exchange. Only web (confidential) applications use client secrets; native (public) applications rely on PKCE instead.

You can generate additional client secrets from the app settings page. This is useful when you need to rotate credentials or deploy to a new environment.

Client secrets do not expire.

### Revoking a secret

If a secret is compromised or no longer needed, revoke it from the app settings. Before revoking, ensure your application is configured with a different valid secret, or users will be unable to complete the OAuth flow.

## Deleting an app

Deleting an OAuth app is immediate and irreversible. All tokens issued through that app become invalid instantly. Users who authorized your app will see it removed from their authorized apps list, and any applications relying on those tokens will fail to authenticate.

To delete an app, scroll to the bottom of the app settings page and click **Delete App**.

## Dynamic client registration management

OAuth apps created through Dynamic Client Registration work differently. They don't appear in the workspace settings UI and must be managed entirely through the API.

When you register a client dynamically, the response includes a registration access token. This token authorizes management operations on that specific client. Store it securely. Without it, you cannot update or delete the client.

Updating a dynamic client will always delete the client secret and create a new one.


# Authorized apps
Source: https://docs.railway.com/integrations/oauth/authorized-apps

Manage applications you've authorized to access your Railway account.



## Viewing authorized apps

To see which applications have access to your Railway account, go to **Account Settings** and navigate to **Apps**. This page lists every OAuth application you've authorized, and what permissions each app has.

For apps with workspace or project scopes, you'll see which specific resources you shared, and can add or remove access to workspaces or projects.

## Revoking access

To completely remove an app's access to your account, click on the app and select **Revoke Access**. This immediately invalidates all tokens the app holds. The app can no longer make API calls on your behalf.

You can always re-authorize the app later. If you visit the app again and go through its OAuth flow, you'll see the consent screen asking you to approve the same (or different) permissions. This is a fresh authorization, not a restoration of the previous one.


# Troubleshooting
Source: https://docs.railway.com/integrations/oauth/troubleshooting

Common issues and solutions for Login with Railway.



## Invalid redirect URI

The redirect_uri in your authorization request must exactly match one of the URIs you registered when creating your OAuth app. This is a strict string comparison, not a URL pattern match.

Common causes of mismatch:
- Trailing slashes: https://app.com/callback vs https://app.com/callback/
- HTTP vs HTTPS: http://localhost:3000 vs https://localhost:3000
- Port differences: https://app.com vs https://app.com:443
- Path differences: /callback vs /oauth/callback

Double-check your registered URIs in the workspace settings and ensure your application uses the exact same string.

## PKCE requirements

Native applications (mobile apps, desktop apps, CLIs, SPAs) must use PKCE. If you're building a native app and your authorization request doesn't include code_challenge and code_challenge_method=S256, the flow will fail.

## Native app token exchange

For public clients (native apps), don't include a client secret. Instead, provide the PKCE code verifier:

If you include a client secret with a native app, the request will fail. Native apps authenticate through PKCE, not secrets.

## Code already used or expired

Authorization codes are single-use and short-lived. If your application attempts to exchange the same code twice, or waits too long before exchanging it, the request fails.

Ensure your token exchange happens immediately after receiving the code, and that your application doesn't retry failed exchanges with the same code.

## No refresh token in response

To receive a refresh token, your authorization request must include both the offline_access scope and prompt=consent.

## Refresh token stopped working

Refresh tokens expire after one year. If a user hasn't used your application in over a year, their refresh token is no longer valid, and they'll need to re-authenticate.

Refresh tokens may also be rotated. When you exchange a refresh token for a new access token, the response includes a refresh_token field. Initially this might be the same value, but it will eventually return a new token. Always store and use the refresh token from your most recent token response.

## Authorization revoked after using refresh token

If your user's authorization is suddenly revoked when using a refresh token, you likely used an old, already-rotated token. As a security measure, using a rotated refresh token immediately revokes the entire authorization. This behavior helps detect potentially leaked tokens. The user will need to re-authorize your application.

To avoid this, always store and use the refresh_token from your most recent token response, even if it appears unchanged.

## Too many refresh tokens

Each user authorization can have a maximum of 100 refresh tokens. If your application requests more than 100 refresh tokens for the same user (for example, by repeatedly going through the full OAuth flow instead of using existing refresh tokens), the oldest tokens are revoked automatically without notice.

## Access token expired

Access tokens last one hour. If API requests start failing with authentication errors, check whether the token has expired. Use your refresh token to obtain a new access token, or if you don't have a refresh token, redirect the user through the OAuth flow again.

## Workspace query returns not authorized

When querying workspaces with a workspace scope, you must also have the email and profile scopes. Without them, the API cannot resolve workspace membership, and the query returns an empty array.

Ensure your authorization request includes all three:

## ID token missing claims

ID tokens do not include user claims like email, name, or picture. To retrieve these, call the /oauth/me endpoint with your access token:

The claims returned depend on which scopes were approved (email for email, profile for name and picture).

## Code Examples

curl -X POST https://backboard.railway.com/oauth/token \
  -d "grant_type=authorization_code" \
  -d "code=AUTH_CODE" \
  -d "redirect_uri=EXACT_REDIRECT_URI" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "code_verifier=YOUR_CODE_VERIFIER"

&scope=openid email profile workspace:viewer

curl https://backboard.railway.com/oauth/me \
  -H "Authorization: Bearer ACCESS_TOKEN"


# Introduction to GraphQL
Source: https://docs.railway.com/integrations/api/graphql-overview

Learn what GraphQL is, why Railway uses it, and how to get started.



## What is GraphQL?

GraphQL is a query language for APIs. Instead of hitting different endpoints to get different pieces of data, you write a query that describes exactly what you want. The server returns nothing more, nothing less.

Here's a simple example. Say you want to fetch a project's name and the names of its services:

Variables:

The response mirrors the shape of your query:

If you also wanted createdAt, you'd add it to your query. If you don't need something, leave it out.

## How is this different from REST?

With a REST API, you typically have multiple endpoints that return fixed data structures:

To get a project with its services, you might need multiple requests, then stitch the data together yourself. Each endpoint returns whatever fields the API designer decided to include.

GraphQL inverts this. There's one endpoint, and you decide what data you need by writing a query.

| REST | GraphQL |
| --- | --- |
| Multiple endpoints | Single endpoint |
| Server decides response shape | Client decides response shape |
| Often requires multiple round-trips | Fetch related data in one request |
| Fixed response structure | Flexible response structure |

## Why does Railway use GraphQL?

**Evolve without versioning.** Adding new fields doesn't break existing queries. Clients only get what they ask for, so new fields are invisible to old clients. No /v1/, /v2/ versioning needed.

**Strongly typed.** Every GraphQL API has a schema that defines valid queries. This means better tooling, auto-generated documentation, and errors caught before runtime.

**Self-documenting.** The schema is always available to explore, which this guide covers below.

## Core concepts

### Queries

Queries read data. They're the GraphQL equivalent of GET requests.

### Mutations

Mutations change data. They're the equivalent of POST, PUT, or DELETE.

Variables:

Notice that mutations also return data. You can ask for fields on the newly created resource in the same request.

### Variables

The mutation example above uses $input. Variables are passed separately from the query as JSON. This keeps queries reusable and makes it easier to work with dynamic values.

### The schema

Every GraphQL API is backed by a schema that defines all available types, queries, and mutations. The schema is what makes autocomplete and validation possible.

## Exploring the schema

The best way to discover what's available in Railway's API is through the GraphiQL playground.

### Using the docs panel

Click the "Docs" button (or press Ctrl/Cmd+Shift+D) to open the documentation explorer. From here you can:

1. **Browse root operations:** Start with Query to see all available queries, or Mutation for all mutations
2. **Search for types:** Use the search box to find types like Project, Service, or Deployment
3. **Navigate relationships:** Click on any type to see its fields, then click on field types to explore further

### Understanding type signatures

GraphQL types follow consistent patterns:

The ! means non-null. When you see String!, a value is guaranteed. When you see String without !, it might be null. For lists, [Service!]! means the list itself is required and every item in it is required.

When a field returns an object type like Service, you must specify which fields you want from it:

Input types define what you pass to mutations:

### Finding available fields

Click on any type in GraphiQL's Docs panel to see its fields. For example, click Project to see id, name, description, services, environments, and more. For mutations, click the input type (like ProjectCreateInput) to see required and optional fields.

### Pro tip: use autocomplete

In GraphiQL's editor, press Ctrl+Space to trigger autocomplete. It shows all valid fields at your current position in the query, with descriptions.

## Pagination

Railway's API uses Relay-style pagination for lists. Instead of returning a flat array, lists are wrapped in edges and node:

This structure enables cursor-based pagination for large datasets.

### Paginating through results

For larger lists, use first to limit results and after to fetch the next page:

The pageInfo object tells you:

- hasNextPage: whether more results exist
- endCursor: the cursor to pass as after to get the next page

## Making your first request

Railway's GraphQL endpoint is:

A GraphQL request is an HTTP POST with a JSON body containing your query. You can use Railway's GraphiQL playground to explore and test queries before writing code, or tools like Apollo Studio or Insomnia.

### Using cURL

### Using JavaScript

### Using Python

## Tips for getting started

**Start small.** Write a simple query that fetches one thing. Once that works, gradually expand to include related data.

**Read the errors.** GraphQL error messages are specific and helpful. If you misspell a field or pass the wrong type, the error tells you exactly what went wrong and what's valid.

**Think in graphs.** Instead of "what endpoint do I call?", think "what data do I need, and how is it connected?" For example, to get a project with its services and each service's latest deployment status:

## Next steps

- **API Cookbook:** Copy-paste examples for common operations
- **Public API Reference:** Authentication, rate limits, and more

## Code Examples

query project($id: String!) {
  project(id: $id) {
    name
    services {
      edges {
        node {
          name
        }
      }
    }
  }
}

{
  "id": "your-project-id"
}

{
  "data": {
    "project": {
      "name": "my-app",
      "services": {
        "edges": [
          { "node": { "name": "api" } },
          { "node": { "name": "postgres" } }
        ]
      }
    }
  }
}

GET /projects/123           â returns project details
GET /projects/123/services  â returns list of services
GET /services/456           â returns one service's details

query {
  me {
    id
    name
    email
  }
}

mutation projectCreate($input: ProjectCreateInput!) {
  projectCreate(input: $input) {
    id
    name
  }
}

{
  "input": {
    "name": "my-new-project"
  }
}

name: String          # Optional string (can be null)
name: String!         # Required string (cannot be null)

services: [Service!]! # Required list of required Service objects

services {      # services is [Service!]!
  id            # pick the fields you want
  name
}

input ProjectCreateInput {
  name: String!       # Required field
  description: String # Optional field
}

services {
  edges {
    node {
      id
      name
    }
  }
}

query deployments($input: DeploymentListInput!, $first: Int, $after: String) {
  deployments(input: $input, first: $first, after: $after) {
    edges {
      node {
        id
        status
        createdAt
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}

https://backboard.railway.com/graphql/v2

curl -X POST https://backboard.railway.com/graphql/v2 \
  -H "Authorization: Bearer $RAILWAY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "query { me { name email } }"}'

const response = await fetch("https://backboard.railway.com/graphql/v2", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${process.env.RAILWAY_TOKEN}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    query: `query { me { name email } }`,
  }),
});

const { data, errors } = await response.json();

import os
import requests

response = requests.post(
    "https://backboard.railway.com/graphql/v2",
    headers={
        "Authorization": f"Bearer {os.environ['RAILWAY_TOKEN']}",
        "Content-Type": "application/json",
    },
    json={
        "query": "query { me { name email } }",
    },
)

data = response.json()

query project($id: String!) {
  project(id: $id) {
    name
    services {
      edges {
        node {
          name
          serviceInstances {
            edges {
              node {
                latestDeployment {
                  status
                }
              }
            }
          }
        }
      }
    }
  }
}


# API cookbook
Source: https://docs.railway.com/integrations/api/api-cookbook

Quick reference for common Railway API operations.



## Quick setup

**GraphQL Endpoint:**


**Authentication:**


Test your connection:

<GraphQLCodeTabs
  query={query {
      me {
        id
        name
        email
      }
    }}
/>

---

## Projects

See Manage Projects for more details.

### List all projects

<GraphQLCodeTabs
  query={query {
      projects {
        edges {
          node {
            id
            name
          }
        }
      }
    }}
/>

### Get project with services

<GraphQLCodeTabs
  query={query project($id: String!) {
      project(id: $id) {
        id
        name
        services {
          edges {
            node { id name }
          }
        }
        environments {
          edges {
            node { id name }
          }
        }
      }
    }}
  variables={{ id: "project-id" }}
  requiredFields={[
    { name: "id", label: "ID", path: "id" }
  ]}
/>

### Create a project

<GraphQLCodeTabs
  query={mutation projectCreate($input: ProjectCreateInput!) {
      projectCreate(input: $input) {
        id
      }
    }}
  variables={{ input: { name: "My Project" } }}
  requiredFields={[
    { name: "name", label: "Name", path: "input.name" }
  ]}
  optionalFields={[
    { name: "input.description", type: "String", description: "Project description" },
    { name: "input.workspaceId", type: "String", description: "Create in a specific workspace" },
    { name: "input.isPublic", type: "Boolean", description: "Make project publicly visible", apiDefault: "false" },
    { name: "input.prDeploys", type: "Boolean", description: "Enable PR deploy environments", apiDefault: "false" },
    { name: "input.defaultEnvironmentName", type: "String", description: "Name for default environment", apiDefault: "production" }
  ]}
/>

---

## Services

See Manage Services for more details.

### Create service from GitHub

<GraphQLCodeTabs
  query={mutation serviceCreate($input: ServiceCreateInput!) {
      serviceCreate(input: $input) {
        id
      }
    }}
  variables={{
    input: {
      projectId: "project-id",
      name: "API",
      source: { repo: "username/repo" }
    }
  }}
  requiredFields={[
    { name: "projectId", label: "Project ID", path: "input.projectId" },
    { name: "name", label: "Name", path: "input.name" },
    { name: "repo", label: "Repo", path: "input.source.repo" }
  ]}
  optionalFields={[
    { name: "input.branch", type: "String", description: "Git branch to deploy" },
    { name: "input.icon", type: "String", description: "Service icon URL" },
    { name: "input.variables", type: "JSON", description: "Initial environment variables" }
  ]}
/>

### Create service from Docker image

<GraphQLCodeTabs
  query={mutation serviceCreate($input: ServiceCreateInput!) {
      serviceCreate(input: $input) {
        id
      }
    }}
  variables={{
    input: {
      projectId: "project-id",
      name: "Ubuntu",
      source: { image: "ubuntu" }
    }
  }}
  requiredFields={[
    { name: "projectId", label: "Project ID", path: "input.projectId" },
    { name: "name", label: "Name", path: "input.name" },
    { name: "image", label: "Image", path: "input.source.image" }
  ]}
  optionalFields={[
    { name: "input.icon", type: "String", description: "Service icon URL" },
    { name: "input.variables", type: "JSON", description: "Initial environment variables" }
  ]}
/>

### Update service settings

<GraphQLCodeTabs
  query={mutation serviceInstanceUpdate($serviceId: String!, $environmentId: String!, $input: ServiceInstanceUpdateInput!) {
      serviceInstanceUpdate(serviceId: $serviceId, environmentId: $environmentId, input: $input)
    }}
  variables={{
    serviceId: "service-id",
    environmentId: "environment-id",
    input: { startCommand: "npm start" }
  }}
  requiredFields={[
    { name: "serviceId", label: "Service ID", path: "serviceId" },
    { name: "environmentId", label: "Environment ID", path: "environmentId" },
    { name: "startCommand", label: "Start Command", path: "input.startCommand" }
  ]}
  optionalFields={[
    { name: "input.buildCommand", type: "String", description: "Custom build command" },
    { name: "input.healthcheckPath", type: "String", description: "Health check endpoint path" },
    { name: "input.numReplicas", type: "Int", description: "Number of replicas", apiDefault: "1" },
    { name: "input.region", type: "String", description: "Deployment region" },
    { name: "input.rootDirectory", type: "String", description: "Root directory for monorepos" },
    { name: "input.cronSchedule", type: "String", description: "Cron schedule for cron jobs" },
    { name: "input.sleepApplication", type: "Boolean", description: "Enable sleep when idle", apiDefault: "false" }
  ]}
/>

---

## Deployments

See Manage Deployments for more details.

### List recent deployments

<GraphQLCodeTabs
  query={query deployments($input: DeploymentListInput!) {
      deployments(input: $input, first: 5) {
        edges {
          node {
            id
            status
            createdAt
          }
        }
      }
    }}
  variables={{
    input: {
      projectId: "project-id",
      serviceId: "service-id"
    }
  }}
  requiredFields={[
    { name: "projectId", label: "Project ID", path: "input.projectId" },
    { name: "serviceId", label: "Service ID", path: "input.serviceId" }
  ]}
/>

### Get deployment logs

<GraphQLCodeTabs
  query={query deploymentLogs($deploymentId: String!, $limit: Int) {
      deploymentLogs(deploymentId: $deploymentId, limit: $limit) {
        timestamp
        message
        severity
      }
    }}
  variables={{ deploymentId: "deployment-id", limit: 100 }}
  requiredFields={[
    { name: "deploymentId", label: "Deployment ID", path: "deploymentId" },
    { name: "limit", label: "Limit", path: "limit" }
  ]}
/>

### Deploy

<GraphQLCodeTabs
  query={mutation serviceInstanceDeploy($serviceId: String!, $environmentId: String!) {
      serviceInstanceDeploy(serviceId: $serviceId, environmentId: $environmentId)
    }}
  variables={{ serviceId: "service-id", environmentId: "environment-id" }}
  requiredFields={[
    { name: "serviceId", label: "Service ID", path: "serviceId" },
    { name: "environmentId", label: "Environment ID", path: "environmentId" }
  ]}
/>

### Rollback

<GraphQLCodeTabs
  query={mutation deploymentRollback($id: String!) {
      deploymentRollback(id: $id) {
        id
      }
    }}
  variables={{ id: "deployment-id" }}
  requiredFields={[
    { name: "id", label: "ID", path: "id" }
  ]}
/>

---

## Variables

See Manage Variables for more details.

### Get variables

<GraphQLCodeTabs
  query={query variables($projectId: String!, $environmentId: String!, $serviceId: String) {
      variables(projectId: $projectId, environmentId: $environmentId, serviceId: $serviceId)
    }}
  variables={{
    projectId: "project-id",
    environmentId: "environment-id",
    serviceId: "service-id"
  }}
  requiredFields={[
    { name: "projectId", label: "Project ID", path: "projectId" },
    { name: "environmentId", label: "Environment ID", path: "environmentId" },
    { name: "serviceId", label: "Service ID", path: "serviceId" }
  ]}
/>

### Set variables

<GraphQLCodeTabs
  query={mutation variableCollectionUpsert($input: VariableCollectionUpsertInput!) {
      variableCollectionUpsert(input: $input)
    }
  }
  variables={{
    input: {
      projectId: "project-id",
      environmentId: "environment-id",
      serviceId: "service-id",
      variables: { KEY1: "value1", KEY2: "value2" }
    }
  }}
  requiredFields={[
    { name: "projectId", label: "Project ID", path: "input.projectId" },
    { name: "environmentId", label: "Environment ID", path: "input.environmentId" },
    { name: "serviceId", label: "Service ID", path: "input.serviceId" },
    { name: "KEY1", label: "KEY1", path: "input.variables.KEY1" },
    { name: "KEY2", label: "KEY2", path: "input.variables.KEY2" }
  ]}
  optionalFields={[
    { name: "input.replace", type: "Boolean", description: "Replace all existing variables", apiDefault: "false" },
    { name: "input.skipDeploys", type: "Boolean", description: "Skip automatic redeploy after change", apiDefault: "false" }
  ]}
/>

---

## Environments

### List environments

<GraphQLCodeTabs
  query={query environments($projectId: String!) {
      environments(projectId: $projectId) {
        edges {
          node {
            id
            name
          }
        }
      }
    }}
  variables={{ projectId: "project-id" }}
  requiredFields={[
    { name: "projectId", label: "Project ID", path: "projectId" }
  ]}
/>

### Create environment

<GraphQLCodeTabs
  query={mutation environmentCreate($input: EnvironmentCreateInput!) {
      environmentCreate(input: $input) {
        id
      }
    }}
  variables={{
    input: {
      projectId: "project-id",
      name: "staging"
    }
  }}
  requiredFields={[
    { name: "projectId", label: "Project ID", path: "input.projectId" },
    { name: "name", label: "Name", path: "input.name" }
  ]}
  optionalFields={[
    { name: "input.sourceEnvironmentId", type: "String", description: "Clone from this environment" },
    { name: "input.ephemeral", type: "Boolean", description: "Create as ephemeral (PR preview)", apiDefault: "false" },
    { name: "input.skipInitialDeploys", type: "Boolean", description: "Don't trigger deploys on creation", apiDefault: "false" }
  ]}
/>

---

## Domains

### Add Railway domain

<GraphQLCodeTabs
  query={mutation serviceDomainCreate($input: ServiceDomainCreateInput!) {
      serviceDomainCreate(input: $input) {
        domain
      }
    }}
  variables={{
    input: {
      serviceId: "service-id",
      environmentId: "environment-id"
    }
  }}
  requiredFields={[
    { name: "serviceId", label: "Service ID", path: "input.serviceId" },
    { name: "environmentId", label: "Environment ID", path: "input.environmentId" }
  ]}
  optionalFields={[
    { name: "input.targetPort", type: "Int", description: "Route traffic to this port" }
  ]}
/>

### Add custom domain

<GraphQLCodeTabs
  query={mutation customDomainCreate($input: CustomDomainCreateInput!) {
      customDomainCreate(input: $input) {
        id
        status {
          dnsRecords {
            hostlabel
            requiredValue
          }
        }
      }
    }}
  variables={{
    input: {
      projectId: "project-id",
      environmentId: "environment-id",
      serviceId: "service-id",
      domain: "api.example.com"
    }
  }}
  requiredFields={[
    { name: "projectId", label: "Project ID", path: "input.projectId" },
    { name: "environmentId", label: "Environment ID", path: "input.environmentId" },
    { name: "serviceId", label: "Service ID", path: "input.serviceId" },
    { name: "domain", label: "Domain", path: "input.domain" }
  ]}
  optionalFields={[
    { name: "input.targetPort", type: "Int", description: "Route traffic to this port" }
  ]}
/>

---

## Volumes

### Create volume

<GraphQLCodeTabs
  query={
    mutation volumeCreate($input: VolumeCreateInput!) {
      volumeCreate(input: $input) {
        id
      }
    }}
  variables={{
    input: {
      projectId: "project-id",
      serviceId: "service-id",
      mountPath: "/data"
    }
  }}
  requiredFields={[
    { name: "projectId", label: "Project ID", path: "input.projectId" },
    { name: "serviceId", label: "Service ID", path: "input.serviceId" },
    { name: "mountPath", label: "Mount Path", path: "input.mountPath" }
  ]}
  optionalFields={[
    { name: "input.environmentId", type: "String", description: "Create in specific environment" },
    { name: "input.region", type: "String", description: "Volume region (e.g., us-west1)" }
  ]}
/>

### Create backup

<GraphQLCodeTabs
  query={
    mutation volumeInstanceBackupCreate($volumeInstanceId: String!) {
      volumeInstanceBackupCreate(volumeInstanceId: $volumeInstanceId)
    }}
  variables={{ volumeInstanceId: "volume-instance-id" }}
  requiredFields={[
    { name: "volumeInstanceId", label: "Volume Instance ID", path: "volumeInstanceId" }
  ]}
/>

---

## TCP proxies

### List TCP proxies

<GraphQLCodeTabs
  query={query tcpProxies($serviceId: String!, $environmentId: String!) {
      tcpProxies(serviceId: $serviceId, environmentId: $environmentId) {
        id
        domain
        proxyPort
        applicationPort
      }
    }}
  variables={{ serviceId: "service-id", environmentId: "environment-id" }}
  requiredFields={[
    { name: "serviceId", label: "Service ID", path: "serviceId" },
    { name: "environmentId", label: "Environment ID", path: "environmentId" }
  ]}
/>

---

## Workspaces

### Get workspace

<GraphQLCodeTabs
  query={query workspace($workspaceId: String!) {
      workspace(workspaceId: $workspaceId) {
        id
        name
        members {
          id
          name
          email
          role
        }
      }
    }}
  variables={{ workspaceId: "workspace-id" }}
  requiredFields={[
    { name: "workspaceId", label: "Workspace ID", path: "workspaceId" }
  ]}
/>

---

## Useful queries

### Get project token info

Use with a project token:

<GraphQLCodeTabs
  query={query {
      projectToken {
        projectId
        environmentId
      }
    }}
/>

### List available regions

<GraphQLCodeTabs
  query={query {
      regions {
        name
        country
        location
      }
    }}
/>

---

## Tips

### Finding IDs

Press Cmd/Ctrl + K in the Railway dashboard and search for "Copy Project ID", "Copy Service ID", or "Copy Environment ID".

### Using the network tab

Do the action in the Railway dashboard and inspect the network tab to see the exact GraphQL queries used.

### GraphiQL playground

Test queries interactively at railway.com/graphiql.

## Code Examples

https://backboard.railway.com/graphql/v2

# Set your token (get one from railway.com/account/tokens)
export RAILWAY_TOKEN="your-token"


# Manage projects
Source: https://docs.railway.com/integrations/api/manage-projects

Learn how to manage projects via the public GraphQL API.



## List all projects

Fetch all projects in your personal account:

<GraphQLCodeTabs query={query {
  projects {
    edges {
      node {
        id
        name
        description
        createdAt
        updatedAt
      }
    }
  }
}} />

### List projects in a workspace

Fetch all projects in a specific workspace:

<GraphQLCodeTabs query={query workspaceProjects($workspaceId: String!) {
  projects(workspaceId: $workspaceId) {
    edges {
      node {
        id
        name
        description
      }
    }
  }
}} variables={{ workspaceId: "workspace-id" }} />

## Get a single project

Fetch a project by ID with its services and environments:

<GraphQLCodeTabs query={query project($id: String!) {
  project(id: $id) {
    id
    name
    description
    createdAt
    services {
      edges {
        node {
          id
          name
          icon
        }
      }
    }
    environments {
      edges {
        node {
          id
          name
        }
      }
    }
  }
}} variables={{ id: "project-id" }} />

## Create a project

Create a new empty project:

<GraphQLCodeTabs query={mutation projectCreate($input: ProjectCreateInput!) {
  projectCreate(input: $input) {
    id
    name
  }
}} variables={{ input: { name: "My New Project" } }}
optionalFields={[
  { name: "input.description", type: "String", description: "Project description" },
  { name: "input.workspaceId", type: "String", description: "Create in a specific workspace" },
  { name: "input.isPublic", type: "Boolean", description: "Make project publicly visible", apiDefault: "false" },
  { name: "input.prDeploys", type: "Boolean", description: "Enable PR deploy environments", apiDefault: "false" },
  { name: "input.defaultEnvironmentName", type: "String", description: "Name for default environment", apiDefault: "production" },
  { name: "input.repo", type: "ProjectCreateRepo", description: "Connect to a GitHub repository" },
]} />

## Update a project

Update project name or description:

<GraphQLCodeTabs query={mutation projectUpdate($id: String!, $input: ProjectUpdateInput!) {
  projectUpdate(id: $id, input: $input) {
    id
    name
    description
  }
}} variables={{ id: "project-id", input: { name: "Updated Project Name" } }}
optionalFields={[
  { name: "input.description", type: "String", description: "Project description" },
  { name: "input.isPublic", type: "Boolean", description: "Make project publicly visible", apiDefault: "false" },
  { name: "input.prDeploys", type: "Boolean", description: "Enable PR deploy environments", apiDefault: "false" },
]} />

## Delete a project

<Banner variant="danger">This is a destructive action and cannot be undone.</Banner>

<GraphQLCodeTabs query={mutation projectDelete($id: String!) {
  projectDelete(id: $id)
}} variables={{ id: "project-id" }} />

## Transfer a project to a workspace

Transfer a project to a different workspace:

<GraphQLCodeTabs query={mutation projectTransfer($projectId: String!, $input: ProjectTransferInput!) {
  projectTransfer(projectId: $projectId, input: $input)
}} variables={{ projectId: "project-id", input: { workspaceId: "target-workspace-id" } }} />

## Get project members

List all members of a project:

<GraphQLCodeTabs query={query projectMembers($projectId: String!) {
  projectMembers(projectId: $projectId) {
    id
    role
    user {
      id
      name
      email
    }
  }
}} variables={{ projectId: "project-id" }} />


# Manage services
Source: https://docs.railway.com/integrations/api/manage-services

Learn how to create and manage services via the public GraphQL API.



## Get a service

Fetch a service by ID:

<GraphQLCodeTabs query={query service($id: String!) {
  service(id: $id) {
    id
    name
    icon
    createdAt
    projectId
  }
}} variables={{ id: "service-id" }} />

## Get a service instance

Get detailed service configuration for a specific environment:

<GraphQLCodeTabs query={query serviceInstance($serviceId: String!, $environmentId: String!) {
  serviceInstance(serviceId: $serviceId, environmentId: $environmentId) {
    id
    serviceName
    startCommand
    buildCommand
    rootDirectory
    healthcheckPath
    region
    numReplicas
    restartPolicyType
    restartPolicyMaxRetries
    latestDeployment {
      id
      status
      createdAt
    }
  }
}} variables={{ serviceId: "service-id", environmentId: "environment-id" }} />

## Create a service

### From a GitHub repository

<GraphQLCodeTabs query={mutation serviceCreate($input: ServiceCreateInput!) {
  serviceCreate(input: $input) {
    id
    name
  }
}} variables={{ input: { projectId: "project-id", name: "My API", source: { repo: "username/repo-name" } } }}
optionalFields={[
  { name: "input.branch", type: "String", description: "Git branch to deploy" },
  { name: "input.icon", type: "String", description: "Service icon URL" },
  { name: "input.variables", type: "JSON", description: "Initial environment variables" },
]} />

### From a Docker image

<GraphQLCodeTabs query={mutation serviceCreate($input: ServiceCreateInput!) {
  serviceCreate(input: $input) {
    id
    name
  }
}} variables={{ input: { projectId: "project-id", name: "Redis", source: { image: "redis:7-alpine" } } }}
optionalFields={[
  { name: "input.icon", type: "String", description: "Service icon URL" },
  { name: "input.variables", type: "JSON", description: "Initial environment variables" },
]} />

### Empty service (no source)

Create an empty service that you can configure later:

<GraphQLCodeTabs query={mutation serviceCreate($input: ServiceCreateInput!) {
  serviceCreate(input: $input) {
    id
    name
  }
}} variables={{ input: { projectId: "project-id", name: "Backend API" } }}
optionalFields={[
  { name: "input.icon", type: "String", description: "Service icon URL" },
  { name: "input.variables", type: "JSON", description: "Initial environment variables" },
]} />

## Update a service

Update service name or icon:

<GraphQLCodeTabs query={mutation serviceUpdate($id: String!, $input: ServiceUpdateInput!) {
  serviceUpdate(id: $id, input: $input) {
    id
    name
    icon
  }
}} variables={{ id: "service-id", input: { name: "Renamed Service" } }}
optionalFields={[
  { name: "input.icon", type: "String", description: "Service icon URL" },
]} />

## Update service instance settings

Update build/deploy settings for a service in a specific environment. Click "Additional options" to see all available settings:

<GraphQLCodeTabs query={mutation serviceInstanceUpdate($serviceId: String!, $environmentId: String!, $input: ServiceInstanceUpdateInput!) {
  serviceInstanceUpdate(serviceId: $serviceId, environmentId: $environmentId, input: $input)
}} variables={{ serviceId: "service-id", environmentId: "environment-id", input: { startCommand: "npm run start" } }}
optionalFields={[
  { name: "input.buildCommand", type: "String", description: "Custom build command" },
  { name: "input.rootDirectory", type: "String", description: "Root directory for monorepos" },
  { name: "input.healthcheckPath", type: "String", description: "Health check endpoint path" },
  { name: "input.healthcheckTimeout", type: "Int", description: "Health check timeout in seconds", apiDefault: "300" },
  { name: "input.region", type: "String", description: "Deployment region (e.g., us-west1)" },
  { name: "input.numReplicas", type: "Int", description: "Number of replicas", apiDefault: "1" },
  { name: "input.restartPolicyType", type: "RestartPolicyType", description: "ON_FAILURE, ALWAYS, or NEVER", apiDefault: "ON_FAILURE" },
  { name: "input.restartPolicyMaxRetries", type: "Int", description: "Max restart retries", apiDefault: "10" },
  { name: "input.cronSchedule", type: "String", description: "Cron schedule (e.g., 0 0 * * *)" },
  { name: "input.sleepApplication", type: "Boolean", description: "Enable sleep when idle", apiDefault: "false" },
  { name: "input.dockerfilePath", type: "String", description: "Custom Dockerfile path" },
  { name: "input.watchPatterns", type: "[String!]", description: "File patterns to watch for changes" },
]} />

## Connect a service to a repo

Connect an existing service to a GitHub repository:

<GraphQLCodeTabs query={mutation serviceConnect($id: String!, $input: ServiceConnectInput!) {
  serviceConnect(id: $id, input: $input) {
    id
  }
}} variables={{ id: "service-id", input: { repo: "username/repo-name", branch: "main" } }} />

## Disconnect a service from a repo

<GraphQLCodeTabs query={mutation serviceDisconnect($id: String!) {
  serviceDisconnect(id: $id) {
    id
  }
}} variables={{ id: "service-id" }} />

## Deploy a service

Trigger a new deployment for a service:

<GraphQLCodeTabs query={mutation serviceInstanceDeployV2($serviceId: String!, $environmentId: String!) {
  serviceInstanceDeployV2(serviceId: $serviceId, environmentId: $environmentId)
}} variables={{ serviceId: "service-id", environmentId: "environment-id" }} />

This returns the deployment ID.

## Redeploy a service

Redeploy the latest deployment:

<GraphQLCodeTabs query={mutation serviceInstanceRedeploy($serviceId: String!, $environmentId: String!) {
  serviceInstanceRedeploy(serviceId: $serviceId, environmentId: $environmentId)
}} variables={{ serviceId: "service-id", environmentId: "environment-id" }} />

## Get resource limits

Get the resource limits for a service instance (returns a JSON object):

<GraphQLCodeTabs query={query serviceInstanceLimits($serviceId: String!, $environmentId: String!) {
  serviceInstanceLimits(serviceId: $serviceId, environmentId: $environmentId)
}} variables={{ serviceId: "service-id", environmentId: "environment-id" }} />

## Delete a service

<Banner variant="danger">This will delete the service and all its deployments.</Banner>

<GraphQLCodeTabs query={mutation serviceDelete($id: String!) {
  serviceDelete(id: $id)
}} variables={{ id: "service-id" }} />


# Manage deployments
Source: https://docs.railway.com/integrations/api/manage-deployments

Learn how to manage deployments via the public GraphQL API.



## List deployments

Get all deployments for a service in an environment:

<GraphQLCodeTabs query={query deployments($input: DeploymentListInput!, $first: Int) {
  deployments(input: $input, first: $first) {
    edges {
      node {
        id
        status
        createdAt
        url
        staticUrl
      }
    }
  }
}} variables={{ input: { projectId: "project-id", serviceId: "service-id", environmentId: "environment-id" }, first: 10 }} />

## Get a single deployment

Fetch a deployment by ID:

<GraphQLCodeTabs query={query deployment($id: String!) {
  deployment(id: $id) {
    id
    status
    createdAt
    url
    staticUrl
    meta
    canRedeploy
    canRollback
  }
}} variables={{ id: "deployment-id" }} />

## Get latest active deployment

Get the currently running deployment:

<GraphQLCodeTabs query={query latestDeployment($input: DeploymentListInput!) {
  deployments(input: $input, first: 1) {
    edges {
      node {
        id
        status
        url
        createdAt
      }
    }
  }
}} variables={{ input: { projectId: "project-id", serviceId: "service-id", environmentId: "environment-id", status: { successfulOnly: true } } }} />

## Get build logs

Fetch build logs for a deployment:

<GraphQLCodeTabs query={query buildLogs($deploymentId: String!, $limit: Int) {
  buildLogs(deploymentId: $deploymentId, limit: $limit) {
    timestamp
    message
    severity
  }
}} variables={{ deploymentId: "deployment-id", limit: 500 }} />

## Get runtime logs

Fetch runtime logs for a deployment:

<GraphQLCodeTabs query={query deploymentLogs($deploymentId: String!, $limit: Int) {
  deploymentLogs(deploymentId: $deploymentId, limit: $limit) {
    timestamp
    message
    severity
  }
}} variables={{ deploymentId: "deployment-id", limit: 500 }}
optionalFields={[
  { name: "filter", type: "String", description: "Filter logs by text" },
  { name: "startDate", type: "DateTime", description: "Start of time range (ISO 8601)" },
  { name: "endDate", type: "DateTime", description: "End of time range (ISO 8601)" },
]} />

## Get HTTP logs

Fetch HTTP request logs for a deployment:

<GraphQLCodeTabs query={query httpLogs($deploymentId: String!, $limit: Int) {
  httpLogs(deploymentId: $deploymentId, limit: $limit) {
    timestamp
    requestId
    method
    path
    httpStatus
    totalDuration
    srcIp
  }
}} variables={{ deploymentId: "deployment-id", limit: 100 }} />

## Trigger a redeploy

Redeploy an existing deployment:

<GraphQLCodeTabs query={mutation deploymentRedeploy($id: String!) {
  deploymentRedeploy(id: $id) {
    id
    status
  }
}} variables={{ id: "deployment-id" }} />

## Restart a deployment

Restart a running deployment without rebuilding:

<GraphQLCodeTabs query={mutation deploymentRestart($id: String!) {
  deploymentRestart(id: $id)
}} variables={{ id: "deployment-id" }} />

## Rollback to a deployment

Rollback to a previous deployment:

<GraphQLCodeTabs query={mutation deploymentRollback($id: String!) {
  deploymentRollback(id: $id) {
    id
    status
  }
}} variables={{ id: "deployment-id" }} />

<Banner variant="info">You can only rollback to deployments that have canRollback: true.</Banner>

## Stop a deployment

Stop a running deployment:

<GraphQLCodeTabs query={mutation deploymentStop($id: String!) {
  deploymentStop(id: $id)
}} variables={{ id: "deployment-id" }} />

## Cancel a deployment

Cancel a deployment that is building or queued:

<GraphQLCodeTabs query={mutation deploymentCancel($id: String!) {
  deploymentCancel(id: $id)
}} variables={{ id: "deployment-id" }} />

## Remove a deployment

Remove a deployment from the history:

<GraphQLCodeTabs query={mutation deploymentRemove($id: String!) {
  deploymentRemove(id: $id)
}} variables={{ id: "deployment-id" }} />

## Deploy a specific service in an environment

Trigger a deployment for a specific service:

<GraphQLCodeTabs query={mutation environmentTriggersDeploy($input: EnvironmentTriggersDeployInput!) {
  environmentTriggersDeploy(input: $input)
}} variables={{ input: { environmentId: "environment-id", projectId: "project-id", serviceId: "service-id" } }} />

## Deployment statuses

| Status | Description |
|--------|-------------|
| BUILDING | Deployment is being built |
| DEPLOYING | Deployment is being deployed |
| SUCCESS | Deployment is running successfully |
| FAILED | Deployment failed to build or deploy |
| CRASHED | Deployment crashed after starting |
| REMOVED | Deployment was removed |
| SLEEPING | Deployment is sleeping (inactive) |
| SKIPPED | Deployment was skipped |
| WAITING | Deployment is waiting for approval |
| QUEUED | Deployment is queued |


# Manage variables
Source: https://docs.railway.com/integrations/api/manage-variables

Learn how to manage environment variables via the public GraphQL API.



## Get variables

Fetch variables for a service in an environment:

<GraphQLCodeTabs query={query variables($projectId: String!, $environmentId: String!, $serviceId: String) {
  variables(
    projectId: $projectId
    environmentId: $environmentId
    serviceId: $serviceId
  )
}} variables={{ projectId: "project-id", environmentId: "environment-id", serviceId: "service-id" }} />

**Response:**


Omit serviceId to get shared variables for an environment instead.

## Get unrendered variables

Get variables with references intact (not resolved):

<GraphQLCodeTabs query={query variables($projectId: String!, $environmentId: String!, $serviceId: String, $unrendered: Boolean) {
  variables(
    projectId: $projectId
    environmentId: $environmentId
    serviceId: $serviceId
    unrendered: $unrendered
  )
}} variables={{ projectId: "project-id", environmentId: "environment-id", serviceId: "service-id", unrendered: true }} />

This returns variables like ${{Postgres.DATABASE_URL}} instead of the resolved value.

## Create or update a variable

Upsert a single variable:

<GraphQLCodeTabs query={mutation variableUpsert($input: VariableUpsertInput!) {
  variableUpsert(input: $input)
}} variables={{ input: { projectId: "project-id", environmentId: "environment-id", serviceId: "service-id", name: "API_KEY", value: "secret-key-here" } }}
optionalFields={[
  { name: "input.skipDeploys", type: "Boolean", description: "Don't trigger a redeploy after change", apiDefault: "false" },
]} />

Omit serviceId to create a shared variable instead.

## Upsert multiple variables

Update multiple variables at once:

<GraphQLCodeTabs query={mutation variableCollectionUpsert($input: VariableCollectionUpsertInput!) {
  variableCollectionUpsert(input: $input)
}} variables={{ input: { projectId: "project-id", environmentId: "environment-id", serviceId: "service-id", variables: { DATABASE_URL: "postgres://...", REDIS_URL: "redis://...", NODE_ENV: "production" } } }}
optionalFields={[
  { name: "input.replace", type: "Boolean", description: "Replace all existing variables (delete any not in the new set)", apiDefault: "false" },
  { name: "input.skipDeploys", type: "Boolean", description: "Don't trigger a redeploy after change", apiDefault: "false" },
]} />

<Banner variant="warning">Using replace: true will delete all variables not included in the variables object.</Banner>

## Delete a variable

Delete a single variable:

<GraphQLCodeTabs query={mutation variableDelete($input: VariableDeleteInput!) {
  variableDelete(input: $input)
}} variables={{ input: { projectId: "project-id", environmentId: "environment-id", serviceId: "service-id", name: "OLD_VARIABLE" } }} />

## Get rendered variables for deployment

Get all variables as they would appear during a deployment (with all references resolved):

<GraphQLCodeTabs query={query variablesForServiceDeployment($projectId: String!, $environmentId: String!, $serviceId: String!) {
  variablesForServiceDeployment(
    projectId: $projectId
    environmentId: $environmentId
    serviceId: $serviceId
  )
}} variables={{ projectId: "project-id", environmentId: "environment-id", serviceId: "service-id" }} />

## Variable references

Railway supports referencing variables from other services using the syntax:

For example, to reference a database URL from a Postgres service:

<GraphQLCodeTabs query={mutation variableUpsert($input: VariableUpsertInput!) {
  variableUpsert(input: $input)
}} variables={{ input: { projectId: "project-id", environmentId: "environment-id", serviceId: "service-id", name: "DATABASE_URL", value: "${{Postgres.DATABASE_URL}}" } }} />

## Common patterns

### Copy variables between environments

1. Fetch variables from source environment
2. Upsert to target environment using variableCollectionUpsert

### Import from .env file

Parse your .env file and use variableCollectionUpsert to set all variables at once.

### Rotate secrets

Use variableUpsert with skipDeploys: true for all services, then trigger deployments manually when ready.

## Code Examples

{
  "data": {
    "variables": {
      "DATABASE_URL": "postgres://...",
      "NODE_ENV": "production",
      "PORT": "3000"
    }
  }
}

${{ServiceName.VARIABLE_NAME}}


# Manage environments
Source: https://docs.railway.com/integrations/api/manage-environments

Learn how to manage environments via the public GraphQL API.



## List environments

Get all environments for a project:

<GraphQLCodeTabs query={query environments($projectId: String!) {
  environments(projectId: $projectId) {
    edges {
      node {
        id
        name
        createdAt
      }
    }
  }
}} variables={{ projectId: "project-id" }} />

### Exclude ephemeral environments

Filter out PR/preview environments:

<GraphQLCodeTabs query={query environments($projectId: String!, $isEphemeral: Boolean) {
  environments(projectId: $projectId, isEphemeral: $isEphemeral) {
    edges {
      node {
        id
        name
        createdAt
      }
    }
  }
}} variables={{ projectId: "project-id", isEphemeral: false }} />

## Get a single environment

Fetch an environment by ID with its service instances:

<GraphQLCodeTabs query={query environment($id: String!) {
  environment(id: $id) {
    id
    name
    createdAt
    serviceInstances {
      edges {
        node {
          id
          serviceName
          latestDeployment {
            id
            status
          }
        }
      }
    }
  }
}} variables={{ id: "environment-id" }} />

## Create an environment

Create a new environment:

<GraphQLCodeTabs query={mutation environmentCreate($input: EnvironmentCreateInput!) {
  environmentCreate(input: $input) {
    id
    name
  }
}} variables={{ input: { projectId: "project-id", name: "staging" } }}
optionalFields={[
  { name: "input.sourceEnvironmentId", type: "String", description: "Clone variables and settings from this environment" },
  { name: "input.ephemeral", type: "Boolean", description: "Create as ephemeral (for PR previews)", apiDefault: "false" },
  { name: "input.skipInitialDeploys", type: "Boolean", description: "Don't trigger deployments on creation", apiDefault: "false" },
  { name: "input.stageInitialChanges", type: "Boolean", description: "Stage changes instead of applying immediately", apiDefault: "false" },
]} />

## Rename an environment

<GraphQLCodeTabs query={mutation environmentRename($id: String!, $input: EnvironmentRenameInput!) {
  environmentRename(id: $id, input: $input)
}} variables={{ id: "environment-id", input: { name: "new-name" } }} />

## Delete an environment

<Banner variant="danger">This will delete the environment and all its deployments.</Banner>

<GraphQLCodeTabs query={mutation environmentDelete($id: String!) {
  environmentDelete(id: $id)
}} variables={{ id: "environment-id" }} />

## Get environment logs

Fetch logs from all services in an environment:

<GraphQLCodeTabs query={query environmentLogs($environmentId: String!, $filter: String) {
  environmentLogs(environmentId: $environmentId, filter: $filter) {
    timestamp
    message
    severity
    tags {
      serviceId
      deploymentId
    }
  }
}} variables={{ environmentId: "environment-id" }}
optionalFields={[
  { name: "filter", type: "String", description: "Filter logs by text (e.g., 'error')" },
]} />

## Staged changes

Railway supports staging variable changes before deploying them.

### Get staged changes

<GraphQLCodeTabs query={query environmentStagedChanges($environmentId: String!) {
  environmentStagedChanges(environmentId: $environmentId)
}} variables={{ environmentId: "environment-id" }} />

### Commit staged changes

<GraphQLCodeTabs query={mutation environmentPatchCommitStaged($environmentId: String!) {
  environmentPatchCommitStaged(environmentId: $environmentId)
}} variables={{ environmentId: "environment-id" }} />


# Manage domains
Source: https://docs.railway.com/integrations/api/manage-domains

Learn how to manage domains via the public GraphQL API.



## List domains for a service

Get all domains (both Railway-provided and custom) for a service:

<GraphQLCodeTabs query={query domains($projectId: String!, $environmentId: String!, $serviceId: String!) {
  domains(
    projectId: $projectId
    environmentId: $environmentId
    serviceId: $serviceId
  ) {
    serviceDomains {
      id
      domain
      suffix
      targetPort
    }
    customDomains {
      id
      domain
      status {
        dnsRecords {
          hostlabel
          requiredValue
          currentValue
          status
        }
      }
    }
  }
}} variables={{ projectId: "project-id", environmentId: "environment-id", serviceId: "service-id" }} />

## Service domains (*.railway.app)

### Create a service domain

Generate a Railway-provided domain:

<GraphQLCodeTabs query={mutation serviceDomainCreate($input: ServiceDomainCreateInput!) {
  serviceDomainCreate(input: $input) {
    id
    domain
  }
}} variables={{ input: { serviceId: "service-id", environmentId: "environment-id" } }}
optionalFields={[
  { name: "input.targetPort", type: "Int", description: "Route traffic to this port" },
]} />

### Delete a service domain

<GraphQLCodeTabs query={mutation serviceDomainDelete($id: String!) {
  serviceDomainDelete(id: $id)
}} variables={{ id: "service-domain-id" }} />

## Custom domains

### Check domain availability

Check if a custom domain can be added:

<GraphQLCodeTabs query={query customDomainAvailable($domain: String!) {
  customDomainAvailable(domain: $domain) {
    available
    message
  }
}} variables={{ domain: "api.example.com" }} />

### Add a custom domain

<GraphQLCodeTabs query={mutation customDomainCreate($input: CustomDomainCreateInput!) {
  customDomainCreate(input: $input) {
    id
    domain
    status {
      dnsRecords {
        hostlabel
        requiredValue
        status
      }
    }
  }
}} variables={{ input: { projectId: "project-id", environmentId: "environment-id", serviceId: "service-id", domain: "api.example.com" } }}
optionalFields={[
  { name: "input.targetPort", type: "Int", description: "Route traffic to this port" },
]} />

### Get custom domain status

Check DNS configuration status:

<GraphQLCodeTabs query={query customDomain($id: String!, $projectId: String!) {
  customDomain(id: $id, projectId: $projectId) {
    id
    domain
    status {
      dnsRecords {
        hostlabel
        requiredValue
        currentValue
        status
      }
      certificateStatus
    }
  }
}} variables={{ id: "custom-domain-id", projectId: "project-id" }} />

### Update a custom domain

<GraphQLCodeTabs query={mutation customDomainUpdate($id: String!, $environmentId: String!, $targetPort: Int) {
  customDomainUpdate(id: $id, environmentId: $environmentId, targetPort: $targetPort)
}} variables={{ id: "custom-domain-id", environmentId: "environment-id", targetPort: 8080 }} />

### Delete a custom domain

<GraphQLCodeTabs query={mutation customDomainDelete($id: String!) {
  customDomainDelete(id: $id)
}} variables={{ id: "custom-domain-id" }} />

## DNS configuration

After adding a custom domain, you need to configure DNS records. The required records are returned in the status.dnsRecords field.

### For root domains (example.com)

Add an A record or ALIAS record pointing to the Railway IP.

### For subdomains (api.example.com)

Add a CNAME record pointing to your Railway service domain.

### DNS record statuses

| Status | Description |
|--------|-------------|
| PENDING | DNS record not yet configured |
| VALID | DNS record is correctly configured |
| INVALID | DNS record is configured incorrectly |

### Certificate statuses

| Status | Description |
|--------|-------------|
| PENDING | Certificate is being issued |
| ISSUED | Certificate is active |
| FAILED | Certificate issuance failed |


# Manage volumes
Source: https://docs.railway.com/integrations/api/manage-volumes

Learn how to manage persistent volumes via the public GraphQL API.



## Get project volumes

List all volumes in a project:

<GraphQLCodeTabs query={query project($id: String!) {
  project(id: $id) {
    volumes {
      edges {
        node {
          id
          name
          createdAt
        }
      }
    }
  }
}} variables={{ id: "project-id" }} />

## Get volume instance details

Get details about a volume instance (volume in a specific environment):

<GraphQLCodeTabs query={query volumeInstance($id: String!) {
  volumeInstance(id: $id) {
    id
    mountPath
    currentSizeMB
    state
    volume {
      id
      name
    }
    serviceInstance {
      serviceName
    }
  }
}} variables={{ id: "volume-instance-id" }} />

## Create a volume

Create a new persistent volume attached to a service:

<GraphQLCodeTabs query={mutation volumeCreate($input: VolumeCreateInput!) {
  volumeCreate(input: $input) {
    id
    name
  }
}} variables={{ input: { projectId: "project-id", serviceId: "service-id", mountPath: "/data" } }}
optionalFields={[
  { name: "input.environmentId", type: "String", description: "Create in a specific environment" },
  { name: "input.region", type: "String", description: "Volume region (e.g., us-west1)" },
]} />

## Update a volume

Rename a volume:

<GraphQLCodeTabs query={mutation volumeUpdate($volumeId: String!, $input: VolumeUpdateInput!) {
  volumeUpdate(volumeId: $volumeId, input: $input) {
    id
    name
  }
}} variables={{ volumeId: "volume-id", input: { name: "database-storage" } }} />

## Update volume instance

Update the mount path for a volume instance:

<GraphQLCodeTabs query={mutation volumeInstanceUpdate($volumeId: String!, $input: VolumeInstanceUpdateInput!) {
  volumeInstanceUpdate(volumeId: $volumeId, input: $input)
}} variables={{ volumeId: "volume-id", input: { mountPath: "/new/path" } }} />

## Delete a volume

<Banner variant="danger">This will permanently delete the volume and all its data.</Banner>

<GraphQLCodeTabs query={mutation volumeDelete($volumeId: String!) {
  volumeDelete(volumeId: $volumeId)
}} variables={{ volumeId: "volume-id" }} />

## Volume backups

### List backups

Get all backups for a volume instance:

<GraphQLCodeTabs query={query volumeInstanceBackupList($volumeInstanceId: String!) {
  volumeInstanceBackupList(volumeInstanceId: $volumeInstanceId) {
    id
    name
    createdAt
    expiresAt
    usedMB
    referencedMB
  }
}} variables={{ volumeInstanceId: "volume-instance-id" }} />

### Create a backup

<GraphQLCodeTabs query={mutation volumeInstanceBackupCreate($volumeInstanceId: String!) {
  volumeInstanceBackupCreate(volumeInstanceId: $volumeInstanceId)
}} variables={{ volumeInstanceId: "volume-instance-id" }} />

### Restore from backup

<GraphQLCodeTabs query={mutation volumeInstanceBackupRestore($volumeInstanceBackupId: String!, $volumeInstanceId: String!) {
  volumeInstanceBackupRestore(volumeInstanceBackupId: $volumeInstanceBackupId, volumeInstanceId: $volumeInstanceId)
}} variables={{ volumeInstanceBackupId: "backup-id", volumeInstanceId: "volume-instance-id" }} />

### Lock a backup (prevent expiration)

<GraphQLCodeTabs query={mutation volumeInstanceBackupLock($volumeInstanceBackupId: String!, $volumeInstanceId: String!) {
  volumeInstanceBackupLock(volumeInstanceBackupId: $volumeInstanceBackupId, volumeInstanceId: $volumeInstanceId)
}} variables={{ volumeInstanceBackupId: "backup-id", volumeInstanceId: "volume-instance-id" }} />

### Delete a backup

<GraphQLCodeTabs query={mutation volumeInstanceBackupDelete($volumeInstanceBackupId: String!, $volumeInstanceId: String!) {
  volumeInstanceBackupDelete(volumeInstanceBackupId: $volumeInstanceBackupId, volumeInstanceId: $volumeInstanceId)
}} variables={{ volumeInstanceBackupId: "backup-id", volumeInstanceId: "volume-instance-id" }} />

## Backup schedules

### List backup schedules

<GraphQLCodeTabs query={query volumeInstanceBackupScheduleList($volumeInstanceId: String!) {
  volumeInstanceBackupScheduleList(volumeInstanceId: $volumeInstanceId) {
    id
    name
    cron
    kind
    retentionSeconds
    createdAt
  }
}} variables={{ volumeInstanceId: "volume-instance-id" }} />

## Common mount paths

| Use Case | Recommended Mount Path |
|----------|------------------------|
| PostgreSQL | /var/lib/postgresql/data |
| MySQL | /var/lib/mysql |
| MongoDB | /data/db |
| Redis | /data |
| General Storage | /data or /app/data |



# Community
Source: https://docs.railway.com/community

# The Conductor program
Source: https://docs.railway.com/community/the-conductor-program

Learn about Railwayâs Conductor Program and how it empowers the developer community.

This program aims to foster collaboration and help Railway's Conductors grow.

## What do conductors do?

Railway's Conductors spend time in Discord and the Central Station answering questions, sharing tips, and making sure everyone can use Railway successfully.

Here are a few key ways they contribute -

- Providing community support through Discord and the Central Station.

- Maintaining a healthy and welcoming community atmosphere while moderating the Railway channels and templates.

- Contributing to Railway's open-source projects through improvements and new features.

- Creating a direct feedback loop between users and the Railway team.

Through these activities, Conductors ensure everyone can use Railway successfully while helping to build a collaborative and supportive community environment.

## Ready to become a conductor?

Are you passionate about helping others and love being part of Railway's community? We're always excited to welcome new Conductors who share Railway's enthusiasm for community engagement!

Here's what we look for in potential Conductors -

- Have demonstrated experience with Railway's platform and services.

- Show a consistent track record of helping others in the Railway community.

- Maintain professional and friendly communication.

- Are active participants in the Discord and Central Station.

- Demonstrate strong technical problem-solving abilities.

The ideal Conductor combines technical expertise with mentorship skills to help the Railway community thrive!

<TallyButton data-tally-open="nP2qqd" data-tally-width="700" data-tally-emoji-text="ð" data-tally-emoji-animation="wave" data-tally-auto-close="2000">Apply Now</TallyButton>

## Conductor benefits

Being a Conductor comes with several exciting perks and rewards to recognize your valuable contributions to the community.

As part of the program, conductors will receive -

- 100% off discount for the Pro plan's subscription and resource costs.

- Cash payouts for solving complex issues for users.

- The opportunity to earn payouts for OSS contributions (CLI, Railpack, Docs, etc).

- First access to template bounties.

- Letters of recommendation for educational institutions and employer references.

- Moderation status on Discord and the Central Station.

- Access to a team workspace shared with other Conductors.

- A direct line to the team via the private Conductor only channel.

- Your choice of Railway Swag.

And to top it all off, each quarter we reward the most outstanding conductor with a pizza party! ð

## Conductor participation

We believe in fostering an active and supportive Conductor program that enables everyone to make meaningful contributions. To help keep the Railway community vibrant, we conduct friendly quarterly check-ins with all Conductors.

As a Conductor, you'll contribute regularly in these key areas -

- Community Engagement

  - Being an active, welcoming presence in community channels.

  - Building connections with fellow community members.

  - Joining community conversations and sharing experiences.

  - Looking out for the community by making sure discussions stay positive and helpful.

- Support Activities

  - Helping others in Discord and the Central Station.

  - Showing consistent engagement by regularly contributing to meaningful solutions across all Railway platforms.

- Open Source Contributions

  - Contributing through either small improvements or substantial feature additions.

  - New features should address community-requested needs with demonstrated user demand.

  - Bug fixes should focus on issues affecting multiple users.

We understand that maintaining consistent participation across these areas requires dedication and time. As part of Railway's commitment to supporting Conductors, we have quarterly check-ins to discuss your experience and ensure you have everything needed to succeed.

While we aim for regular engagement, we recognize that life circumstances and priorities can change. If participation becomes limited, we may need to transition members out of the program during the bi-annual review. However, the door always remains open â former Conductors are welcome to rejoin the program when their schedule better accommodates regular participation!


# Affiliate program
Source: https://docs.railway.com/community/affiliate-program

Show Railway to your network, earn 15% cash commission on referral revenue.

Anyone that signs up from your link will receive $20 in Railway credits, equivalent to a free month on the Pro tier.

Once the signup becomes a Railway customer, you will receive 15% commission on the first 12 months of invoices from the new customer moving forward.

## How do I become an affiliate?

<Image src="https://res.cloudinary.com/railway/image/upload/v1631917786/docs/referrals_cash_ashj73.png"
alt="Screenshot of Referrals Page"
layout="intrinsic"
width={1784} height={1104} quality={80} />

Follow these steps to start earning:

- Sign up for Railway.

- Click the Refer button in the dashboard, or navigate directly to the workspace's <a href="https://railway.com/account/referrals" target="_blank">referrals page</a>.

- Copy the unique link.

- Create content and post about Railway, including the unique link.

To see and withdraw earnings:

- Navigate to the workspace settings and click on Earnings, which leads you to the <a href="https://railway.com/account/earnings" target="_blank">earnings page</a>.

- The Earnings page displays total earnings

- Follow the instructions here to withdraw to GitHub Sponsors or Buy Me a Coffee.

- After adding your account details you will request a withdrawal. The Railway team will receive the request and process it.

## How do I maximize earnings?

Earnings come from signups that are successful and start to scale on Railway. Walk through Railway use cases to give your network an accurate idea of what they can do on Railway.

A few ideas to maximize reach and earnings as an affiliate:

- Create video content on YouTube demoing a use case with a specific template on Railway

- Write a blog post on Medium walking through pros/cons of cloud deployment and hosting on Railway

- Post on LinkedIn (or your social platform of choice) about your experience on Railway


# Bounties
Source: https://docs.railway.com/community/bounties

Learn how to earn money by helping others in the community.



## How bounties work

Bounties are questions from the community that have a cash reward attached. When your answer is accepted as the solution, the bounty amount is added to your Railway earnings. You can use this as Railway credits or withdraw as cash.

### The bounty lifecycle

1. **Question Posted:** A user asks a question in Central Station.
2. **Bounty Created:** Railway marks the question as bounty-eligible and it appears on the Bounty Board.
3. **Community Responds:** Anyone can reply with a helpful answer.
4. **Solution Accepted:** The original poster (or a moderator) marks a reply as the accepted solution. **If someone solves your problem, be a good community member and mark their reply as the solution!**
5. **Review & Payout:** Railway reviews the solution and processes the payout.

## Finding bounties

All active bounties are listed on the Bounty Board. You can also opt-in to receive email notifications when new bounties are posted by flipping the "**Subscribe to bounties**" switch on the Bounty Board.

## When questions become bounties

Railway reviews questions in Central Station and selects some to become bounties. When your question is selected:

- You'll receive an email notification letting you know your question was added to the Bounty Board.
- Your question becomes visible on the Bounty Board where the community can help answer it.
- You don't need to do anything differently. Just wait for helpful answers and mark one as the solution when your problem is solved.

### Why some questions are selected

Not every question becomes a bounty. Railway looks for questions that are:

- **Clear and well-written:** Enough context is provided for someone to understand and help with the problem.
- **Relevant:** About Railway usage, deployment, configuration, or troubleshooting.
- **Answerable:** The question has a concrete answer or solution, not just open-ended discussion.

## Bounty amounts

Bounty amounts vary depending on the question. The standard bounty is **$10 USD**, but some bounties may offer more for complex questions or high-priority topics.

You can see the bounty amount displayed on each question in the Bounty Board, as well as beneath the initial post when viewing an individual thread.

## Requesting a bounty

You can submit your own question as a bounty request in Central Station. This is useful if you have a question you think would benefit from community input and you'd like to incentivize a quick, high-quality answer.

### How to submit a request

1. Go to the Bounty Board and click to create a new bounty.
2. Enter a clear title and detailed description of your question.
3. Submit your request.

Your request creates a private thread visible only to you and the Railway team. You'll be redirected to this thread after submitting.

### What happens next

Railway reviews your request to determine if it's a good fit for the bounty program. During this review, the team considers whether the question is clear, relevant to Railway, and likely to benefit from community answers.

**If your request is approved:**

- Your question is made public and added to the Bounty Board.
- You'll receive an email notification confirming your question is now a bounty.
- The community can start answering, and you can mark the best answer as the solution.
- Railway funds 100% of the bounty reward. You don't pay anything.

**If your request is not approved:**

- Your thread remains private between you and Railway.
- It will be treated like any other private thread in Central Station.

### Tips for getting your request approved

To increase the chances of your bounty request being approved:

- **Be specific:** Clearly describe the problem you're trying to solve.
- **Provide context:** Include relevant details like error messages, configuration, or what you've already tried.
- **Keep it focused:** Ask one clear question rather than multiple questions in one request.
- **Make it relevant:** Questions about Railway deployment, configuration, or troubleshooting are most likely to be approved.

## Earning from bounties

When your answer is accepted as the solution to a bounty question, you receive the bounty amount as earnings. Your bounty earnings appear on your workspace's Earnings page alongside any template and referral earnings.

### Requirements for payout

For a bounty to be awarded, the following must be true:

- **Your answer is marked as the solution:** The original poster, a Conductor, or a Railway team member must mark your reply as the accepted solution.
- **Your answer solves the problem:** Railway reviews accepted solutions before processing payouts to verify the answer is genuinely helpful.
- **You're not the person who asked the question:** You cannot win a bounty on your own question.

If an accepted solution doesn't actually solve the problem, Railway may reject it and reopen the bounty for others to answer.

### Workspace selection

Bounty earnings are deposited to your workspace. If you have multiple workspaces, you can choose which one receives your earnings by clicking "Preferred Bounty Workspace" on the Bounty Board.

## Withdrawing your earnings

You can use your bounty earnings as Railway credits or withdraw them as cash.

### Using earnings as credits

Your earnings balance is available on the Earnings page and can be applied toward your Railway usage.

### Cash withdrawals

If you prefer to withdraw your earnings as cash:

1. Go to your workspace's Earnings page.
2. Set up your cash withdrawal account by connecting Stripe Connect.
3. Withdraw your available balance.

Once Stripe Connect is set up, you can withdraw earnings from bounties, templates, and referrals, all from the same page.

## Notifications

### For question askers

If your question is selected to become a bounty, you'll receive an email notification letting you know it's been added to the Bounty Board.

### For bounty hunters

You can opt-in to receive email notifications whenever a new bounty is posted by flipping the "**Subscribe to bounties**" switch on the Bounty Board.

### For bounty winners

When your answer is accepted and the payout is processed, you'll receive an email confirmation with:

- The bounty amount awarded
- The question you answered
- The workspace where the earnings were deposited

## Tips for winning bounties

Here are some ways to increase your chances of having your answer accepted:

- **Be clear and specific:** Explain your solution step-by-step so anyone can follow along.
- **Include relevant context:** Reference documentation, configuration examples, or code snippets where helpful.
- **Test your solution:** If possible, verify your answer works before posting.
- **Be respectful:** Remember there's a person on the other end who needs help.

## Top contributors

Central Station recognizes top bounty contributors based on activity over the last 30 days. Active participants earn contributor badges (Top 1%, Top 5%, Top 10%) that appear next to their name throughout Central Station.

## Getting started

Ready to start earning?

1. Visit the Bounty Board to see open bounties.
2. Find a question you can help with.
3. Post a helpful, detailed answer.
4. If your answer is accepted and verified, you earn the bounty amount.
5. Set up your withdrawal account on your Earnings page.
6. Withdraw your earnings as cash or use them as Railway credits.

The more you help, the more you earn. Plus, you'll be contributing to a community that helps developers ship faster.



