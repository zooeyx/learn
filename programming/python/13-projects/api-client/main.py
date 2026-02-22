"""API Client — consume a REST API.

Example: Fetch data from JSONPlaceholder (fake REST API).
"""

# TODO: pip install requests
# import requests


def fetch_users(base_url="https://jsonplaceholder.typicode.com"):
    """Fetch list of users from the API."""
    # TODO: GET /users and return JSON
    # Hint: response = requests.get(f"{base_url}/users")
    # Hint: response.raise_for_status()
    # Hint: return response.json()
    return []


def fetch_user_posts(user_id, base_url="https://jsonplaceholder.typicode.com"):
    """Fetch posts for a specific user."""
    # TODO: GET /posts?userId=<id> and return JSON
    return []


def display_user(user):
    """Format and display user info."""
    # TODO: Print user details nicely
    # Hint: print(f"  {user['name']} (@{user['username']})")
    # Hint: print(f"  Email: {user['email']}")
    pass


def main():
    print("API Client")
    print("TODO: Install dependencies: pip install requests")
    print("TODO: Implement fetch_users(), fetch_user_posts(), display_user()")

    # TODO: Uncomment and implement:
    # users = fetch_users()
    # print(f"Found {len(users)} users:\n")
    # for user in users[:3]:
    #     display_user(user)
    #     posts = fetch_user_posts(user["id"])
    #     print(f"  Posts: {len(posts)}\n")


if __name__ == "__main__":
    main()
