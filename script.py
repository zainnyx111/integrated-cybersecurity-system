import subprocess


# -------------------------------
# MODULE 1: PHISHING DETECTION
# -------------------------------
def phishing_detection():
    print("\n--- Phishing Detection Module ---")
    email_text = input("Enter email text or URL: ").lower()

    phishing_keywords = [
        "verify your account",
        "click here",
        "urgent",
        "login immediately",
        "update your password",
        "suspended"
    ]

    score = 0
    for keyword in phishing_keywords:
        if keyword in email_text:
            score += 1

    if score >= 3:
        print(" Result: Phishing Email Detected")
    elif score == 2:
        print(" Result: Suspicious Email")
    else:
        print(" Result: Email Appears Safe")


# -------------------------------
# MODULE 2: VULNERABILITY SCANNING
# -------------------------------
def vulnerability_scan():
    print("\n--- Vulnerability Scanning Module ---")
    target = input("Enter target IP address ")

    try:
        print("\nRunning nmap scan...\n")
        result = subprocess.check_output(
            ["nmap", "-F", target],
            stderr=subprocess.STDOUT
        )
        print(result.decode())
    except Exception as e:
        print("Error running nmap:", e)


# -------------------------------
# MODULE 3: INTRUSION DETECTION
# -------------------------------
def intrusion_detection():
    print("\n--- Intrusion Detection Module ---")
    try:
        failed_attempts = int(input("Enter number of failed login attempts: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if failed_attempts > 5:
        print("Alert: Possible Brute-Force Attack Detected!")
    else:
        print("No intrusion detected.")

# -------------------------------
# MAIN MENU
# -------------------------------
def main():
    while True:
        print("\n==============================")
        print(" Integrated Cybersecurity System ")
        print("==============================")
        print("1. Phishing Detection")
        print("2. Vulnerability Scanning")
        print("3. Intrusion Detection")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            phishing_detection()
        elif choice == "2":
            vulnerability_scan()
        elif choice == "3":
            intrusion_detection()
        elif choice == "4":
            print("Exiting system. Stay secure!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
