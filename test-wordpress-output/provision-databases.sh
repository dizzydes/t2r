#!/bin/bash
#
# Database Provisioning Script for Railway
# Run this after creating your Railway project
#

set -e

echo '🗄️  Provisioning databases...'

# wordpress-db
# Note: Migrated from RDS Aurora cluster
echo 'Creating postgres database: wordpress-db...'
railway add --database postgres

echo '✅ Database provisioning complete!'
echo ''
echo 'Database credentials are automatically injected as environment variables:'
echo '  - DATABASE_URL'
echo '  - REDIS_URL (if Redis was added)'
echo ''
echo 'View variables with: railway variables'