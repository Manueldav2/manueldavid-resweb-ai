# Heroku Deployment Guide

Complete step-by-step guide to deploy the Manuel David Portfolio Chatbot to Heroku.

## Prerequisites

1. **Heroku Account**: Sign up at [heroku.com](https://heroku.com)
2. **Heroku CLI**: Install from [devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)
3. **OpenAI API Key**: Get from [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
4. **Git**: Ensure git is installed and configured

## Step 1: Verify Files

Make sure your directory contains these files:
```
portfolio-chatbot-backend/
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── README.md
├── .gitignore
├── env_config.txt
├── test_chatbot.py
└── DEPLOYMENT.md
```

## Step 2: Login to Heroku

```bash
heroku login
```

This will open your browser to authenticate.

## Step 3: Create Heroku App

```bash
# Navigate to your project directory
cd portfolio-chatbot-backend

# Create a new Heroku app (choose a unique name)
heroku create manuel-portfolio-chatbot

# Or let Heroku generate a name
heroku create
```

## Step 4: Set Environment Variables

```bash
# Set your OpenAI API key
heroku config:set OPENAI_API_KEY=your_actual_openai_api_key_here

# Verify it was set
heroku config
```

## Step 5: Initialize Git and Deploy

```bash
# Initialize git repository
git init

# Add Heroku remote (if not already added)
heroku git:remote -a your-app-name

# Add all files
git add .

# Commit files
git commit -m "Initial deployment of Manuel David portfolio chatbot"

# Deploy to Heroku
git push heroku main
```

## Step 6: Verify Deployment

```bash
# Check if app is running
heroku ps:scale web=1

# View logs
heroku logs --tail

# Open the app
heroku open
```

## Step 7: Test the API

Test the health endpoint:
```bash
curl https://your-app-name.herokuapp.com/health
```

Test the chat endpoint:
```bash
curl -X POST https://your-app-name.herokuapp.com/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me about Manuel David"}'
```

## Step 8: Update Frontend CORS

Add your Heroku URL to the ALLOWED_ORIGINS in `app.py`:
```python
ALLOWED_ORIGINS = [
    'https://your-portfolio-domain.com',
    'https://your-app-name.herokuapp.com',
    'http://localhost:3000'
]
```

Then redeploy:
```bash
git add app.py
git commit -m "Update CORS origins"
git push heroku main
```

## Useful Heroku Commands

```bash
# View app info
heroku info

# View logs
heroku logs --tail

# Check dyno status
heroku ps

# Scale dynos
heroku ps:scale web=1

# Access the Heroku console
heroku run python

# View environment variables
heroku config

# Set environment variable
heroku config:set KEY=value

# Remove environment variable
heroku config:unset KEY

# Restart the app
heroku restart
```

## Troubleshooting

### App Not Starting
1. Check logs: `heroku logs --tail`
2. Verify Procfile exists and is correct
3. Ensure requirements.txt includes all dependencies

### OpenAI API Errors
1. Verify API key is set: `heroku config`
2. Check OpenAI account has credits
3. Ensure API key has correct permissions

### CORS Issues
1. Add your frontend domain to ALLOWED_ORIGINS
2. Redeploy after making changes
3. Check browser developer console for CORS errors

### Performance Issues
1. Upgrade to paid dyno for better performance
2. Monitor response times in logs
3. Consider implementing caching

## Frontend Integration

Once deployed, update your Next.js frontend to use the Heroku URL:

```javascript
const CHATBOT_API_URL = 'https://your-app-name.herokuapp.com/api/chat';

const sendMessage = async (message) => {
  try {
    const response = await fetch(CHATBOT_API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message })
    });
    
    const data = await response.json();
    
    if (response.ok) {
      return data.response;
    } else {
      throw new Error(data.error || 'API error');
    }
  } catch (error) {
    console.error('Chatbot error:', error);
    return 'Sorry, I encountered an error. Please try again.';
  }
};
```

## Cost Considerations

- **Heroku Free Tier**: App sleeps after 30 minutes of inactivity
- **Hobby Dyno ($7/month)**: No sleeping, better for production
- **OpenAI Costs**: Pay per API request, monitor usage in OpenAI dashboard

## Security Best Practices

1. Never commit API keys to git
2. Use environment variables for all secrets
3. Regularly rotate API keys
4. Monitor API usage and set billing alerts
5. Keep dependencies updated

## Success Checklist

- [ ] App deploys without errors
- [ ] Health endpoint returns 200
- [ ] Chat endpoint responds correctly
- [ ] CORS allows frontend requests
- [ ] OpenAI API key is working
- [ ] Logs show no errors
- [ ] Frontend can communicate with backend

Your chatbot should now be live and ready to answer questions about Manuel David! 