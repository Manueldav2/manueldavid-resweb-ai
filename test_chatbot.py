#!/usr/bin/env python3
"""
Test script for Manuel David Portfolio Chatbot
Run this to test the chatbot locally or on Heroku
"""

import requests
import json
import sys

# Configuration
BASE_URL = "http://localhost:5000"  # Change this to your Heroku URL when deployed
# BASE_URL = "https://your-chatbot-app-name.herokuapp.com"

def test_health():
    """Test the health endpoint"""
    print("🔍 Testing health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_knowledge():
    """Test the knowledge endpoint"""
    print("\n🔍 Testing knowledge endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/knowledge")
        print(f"Status: {response.status_code}")
        data = response.json()
        print(f"Response: {json.dumps(data, indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Knowledge test failed: {e}")
        return False

def test_chat(message):
    """Test the chat endpoint with a specific message"""
    print(f"\n🔍 Testing chat with message: '{message}'")
    try:
        response = requests.post(
            f"{BASE_URL}/api/chat",
            headers={"Content-Type": "application/json"},
            json={"message": message}
        )
        print(f"Status: {response.status_code}")
        data = response.json()
        
        if response.status_code == 200:
            print(f"✅ Success!")
            print(f"Response: {data.get('response', 'No response')}")
        else:
            print(f"❌ Error: {data.get('error', 'Unknown error')}")
        
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Chat test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🤖 Manuel David Portfolio Chatbot Test Suite")
    print("=" * 50)
    
    # Test questions
    test_questions = [
        "Tell me about Manuel David",
        "What projects has Manuel built?",
        "How can I contact Manuel?",
        "What are Manuel's skills in AI?",
        "Tell me about the Resume Site AI project",
        "What is Manuel's favorite food?"  # This should return "I don't know"
    ]
    
    # Run tests
    health_ok = test_health()
    knowledge_ok = test_knowledge()
    
    chat_results = []
    for question in test_questions:
        result = test_chat(question)
        chat_results.append(result)
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST SUMMARY")
    print(f"Health endpoint: {'✅ PASS' if health_ok else '❌ FAIL'}")
    print(f"Knowledge endpoint: {'✅ PASS' if knowledge_ok else '❌ FAIL'}")
    print(f"Chat tests passed: {sum(chat_results)}/{len(chat_results)}")
    
    all_passed = health_ok and knowledge_ok and all(chat_results)
    print(f"Overall: {'✅ ALL TESTS PASSED' if all_passed else '❌ SOME TESTS FAILED'}")
    
    if not all_passed:
        print("\n💡 Troubleshooting:")
        print("1. Make sure the server is running")
        print("2. Check your OpenAI API key is set")
        print("3. Verify the BASE_URL is correct")
        sys.exit(1)

if __name__ == "__main__":
    main() 