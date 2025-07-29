# Manuel David Portfolio Chatbot Backend

An AI-powered chatbot backend that knows everything about Manuel David's professional portfolio, projects, and experience. Built with Flask and OpenAI GPT-4.

## Features

- 🤖 **Intelligent Responses**: Powered by OpenAI GPT-4 with comprehensive knowledge about Manuel David
- 📚 **Complete Knowledge Base**: Includes all projects, skills, experience, and contact information
- 🚫 **Bounded Knowledge**: Only answers questions based on available information, politely declines unknown queries
- 🌐 **CORS Ready**: Configured for cross-origin requests from portfolio website
- ⚡ **Production Ready**: Optimized for Heroku deployment with gunicorn

## Knowledge Base Includes

- **Personal Information**: Contact details, location, company
- **Professional Summary**: Experience, specializations, career goals
- **6 Major Projects**: Resume Site AI, Cold Email SaaS, Therapist AI, Nouvo Platform, Popup Drink Website, Business Websites Portfolio
- **Technical Skills**: Frontend, backend, AI/ML, databases, tools
- **Metrics**: Years of experience, projects completed, client satisfaction

## API Endpoints

### `POST /api/chat`
Main chatbot endpoint for asking questions about Manuel David.

**Request:**
```json
{
  "message": "Tell me about Manuel's AI projects"
}
```

**Response:**
```json
{
  "response": "Manuel has developed several impressive AI projects...",
  "status": "success"
}
```

### `GET /health`
Health check endpoint.

### `GET /api/knowledge`
Returns basic information about the knowledge base (for testing).

## Deployment to Heroku

### Prerequisites
- Heroku CLI installed
- OpenAI API key

### Step 1: Create Heroku App
```bash
heroku create your-chatbot-app-name
```

### Step 2: Set Environment Variables
```bash
heroku config:set OPENAI_API_KEY=your_openai_api_key_here
```

### Step 3: Deploy
```bash
git init
git add .
git commit -m "Initial commit"
git push heroku main
```

### Step 4: Test the Deployment
```bash
curl https://your-chatbot-app-name.herokuapp.com/health
```

## Frontend Integration

Add this to your Next.js portfolio website:

```javascript
const sendMessage = async (message) => {
  try {
    const response = await fetch('https://your-chatbot-app-name.herokuapp.com/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message })
    });
    
    const data = await response.json();
    return data.response;
  } catch (error) {
    console.error('Chatbot error:', error);
    return 'Sorry, I encountered an error. Please try again.';
  }
};
```

## Local Development

1. **Clone and setup:**
```bash
cd portfolio-chatbot-backend
pip install -r requirements.txt
```

2. **Set environment variables:**
```bash
export OPENAI_API_KEY=your_key_here
export FLASK_ENV=development
```

3. **Run the app:**
```bash
python app.py
```

4. **Test locally:**
```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me about Manuel"}'
```

## Example Interactions

**Q:** "What projects has Manuel built?"
**A:** Lists all 6 projects with descriptions and technologies

**Q:** "How can I contact Manuel?"
**A:** Provides email and phone number

**Q:** "What is Manuel's favorite food?"
**A:** "I'm sorry, I don't have that specific information about Manuel in my knowledge base..."

## Configuration

The chatbot is configured to:
- Only answer questions about information in the knowledge base
- Respond professionally and enthusiastically about Manuel's work
- Provide specific technical details about projects
- Direct users to contact Manuel for information not in the knowledge base

## Security

- CORS is configured for specific allowed origins
- Input validation on all requests
- Rate limiting through OpenAI API
- Error handling for API failures

## Technologies Used

- **Flask**: Web framework
- **OpenAI GPT-4**: AI language model
- **Flask-CORS**: Cross-origin resource sharing
- **Gunicorn**: WSGI HTTP Server for production
- **Python-dotenv**: Environment variable management

## License

Private project for Manuel David's portfolio website. # manueldavid-resweb-ai
