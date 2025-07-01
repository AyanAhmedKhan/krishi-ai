# 🔑 API Configuration Guide

## **Groq API Setup**

Your Krishi AI-Mitra application uses Groq's Llama 3 model for AI-powered fertilizer recommendations. Follow these steps to configure your API key:

### **Step 1: Get Your Groq API Key**

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in to your account
3. Navigate to "API Keys" section
4. Create a new API key
5. Copy the API key (it starts with `gsk_...`)

### **Step 2: Configure the API Key**

**Option A: Environment Variable (Recommended)**

Set the environment variable before starting your Django server:

```bash
# Windows Command Prompt
set GROQ_API_KEY=gsk_your_api_key_here

# Windows PowerShell
$env:GROQ_API_KEY="gsk_your_api_key_here"

# Linux/Mac
export GROQ_API_KEY=gsk_your_api_key_here
```

**Option B: Direct in Settings**

Edit `krishi_ai_mitra/settings.py` and replace line 18:

```python
GROQ_API_KEY = 'gsk_your_api_key_here'
```

### **Step 3: Test the Configuration**

1. Restart your Django server
2. Visit the fertilizer recommendation tool
3. Try getting a recommendation
4. You should see AI-generated advice instead of the error message

### **Step 4: Security Notes**

- **Never commit your API key** to version control
- **Use environment variables** in production
- **Keep your API key secure** and don't share it
- **Monitor your API usage** in the Groq console

---

## **Troubleshooting**

### **"API key not set" Error**
- Make sure you've set the environment variable correctly
- Restart your Django server after setting the variable
- Check that the API key is valid and active

### **"Rate limit exceeded" Error**
- Groq has rate limits on free accounts
- Consider upgrading your plan for higher limits
- Implement caching to reduce API calls

### **"Model not available" Error**
- The Llama 3 model should be available on all Groq accounts
- Check your Groq console for model availability
- Contact Groq support if issues persist

---

## **Alternative: Use Without AI**

If you don't want to use the Groq API, the fertilizer tool will still work with database recommendations. You just need to:

1. Add crops, soil types, regions, and fertilizers to the admin panel
2. Create fertilizer recommendations in the database
3. The tool will use database recommendations instead of AI

---

**Need Help?** Check the Groq documentation or contact support if you encounter issues. 