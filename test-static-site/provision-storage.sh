#!/bin/bash
#
# Storage Provisioning Script for Railway
# Run this after creating your Railway project
#

set -e

echo '💾 Provisioning storage...'

# site-content
# Note: Migrating AWS S3 bucket for site content. Using sjc (US West) as default region.
echo 'Creating S3-compatible bucket: site-content...'
railway bucket create site-content --region sjc

echo '✅ Storage provisioning complete!'
echo ''
echo 'Bucket credentials are available via:'
echo '  railway bucket credentials --bucket <bucket-name> --json'
echo ''