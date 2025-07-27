# Configuration Directory

This directory contains configuration files for the web crawler.

## Required Files

### mail_config.txt
Create this file with your Gmail credentials for email reporting:
email=your.email@gmail.com
pw=your16characterapppassword

## Setup Instructions

1. **Enable 2-Step Verification** on your Gmail account
2. **Generate an App Password:**
   - Go to myaccount.google.com
   - Security → 2-Step Verification → App passwords
   - Create a new app password for "Web Crawler"
3. **Create mail_config.txt** with your email and the 16-character app password
4. **Verify the file is ignored by Git** (it should not appear in git status)

## Security Note

Never commit `mail_config.txt` to version control. It contains sensitive credentials and is ignored by `.gitignore`.
