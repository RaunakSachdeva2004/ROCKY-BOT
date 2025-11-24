try:
    from langchain.chains import RetrievalQAWithSourcesChain
    print("✅ SUCCESS: langchain.chains is working!")
except ImportError as e:
    print(f"❌ ERROR: {e}")