def verify_access_environment(func):
    def wrapper(*args, **kwargs):
        env = get_environment()
        if env == 'production':
            print("Access was allowed in the production environment")
            return func(*args, **kwargs)
        
        print("Access is restricted to production environments")
    return wrapper

@verify_access_environment
def upload_document(document):
    print(f"Document {document} uploaded")

@verify_access_environment
def delete_document(document):
    print(f"Document {document} deleted")

def get_environment():
    return 'production'

delete_document('234y892')