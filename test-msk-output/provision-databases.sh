#!/bin/bash
#
# Database Provisioning Script for Railway
# Run this after creating your Railway project
#

set -e

echo '🗄️  Provisioning databases...'

# message-queue
# Note: For basic message queueing needs that don't require Kafka
echo 'Creating redis database: message-queue...'
railway add --database redis

echo '✅ Database provisioning complete!'
echo ''
echo 'Database credentials are automatically injected as environment variables:'
echo '  - DATABASE_URL'
echo '  - REDIS_URL (if Redis was added)'
echo ''
echo 'View variables with: railway variables'