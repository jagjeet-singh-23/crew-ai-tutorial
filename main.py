from agents import EmailAgent


def main():
    user_prompt = "Write an email to John Doe about the meeting tomorrow."
    email_agent = EmailAgent()
    agent_response = email_agent.invoke(user_prompt)

    return agent_response


if __name__ == "__main__":
    main()
