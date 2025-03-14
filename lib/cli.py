from worker import Worker
from job import Job
from tabulate import tabulate

def main_menu():
    while True:
        print("\n--- Blue Collar Booking App ---")
        print("1. Manage Workers")
        print("2. Manage Jobs")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            worker_menu()
        elif choice == "2":
            job_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def worker_menu():
    while True:
        print("\n--- Worker Management ---")
        print("1. Add Worker")
        print("2. View All Workers")
        print("3. Delete Worker")
        print("4. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter worker name: ")
            skill = input("Enter worker skill: ")
            worker = Worker.create(name, skill)
            print(f"Worker {worker.name} added.")
        elif choice == "2":
            workers = Worker.get_all()
            print(tabulate([(w.id, w.name, w.skill) for w in workers], headers=["ID", "Name", "Skill"]))
        elif choice == "3":
            worker_id = input("Enter Worker ID to delete: ")
            if Worker.delete(int(worker_id)):
                print("Worker deleted.")
            else:
                print("Worker not found.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def job_menu():
    while True:
        print("\n--- Job Management ---")
        print("1. Add Job")
        print("2. View All Jobs")
        print("3. Delete Job")
        print("4. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter job title: ")
            worker_id = input("Enter Worker ID: ")
            if not worker_id.isdigit():
                print("Error: Worker ID must be a number. Please try again.")
                continue
            try:
                job = Job.create(title, int(worker_id))
            except ValueError:
                print("Error: Invalid Worker ID format. Please enter a valid number.")
                continue
            except Exception as e:
                print(f"Error creating job: {str(e)}. Please verify the Worker ID exists.")
                continue
            print(f"Job {job.title} added.")
        elif choice == "2":
            jobs = Job.get_all()
            print(tabulate([(j.id, j.title, j.worker_id) for j in jobs], headers=["ID", "Title", "Worker ID"]))
        elif choice == "3":
            job_id = input("Enter Job ID to delete: ")
            if Job.delete(int(job_id)):
                print("Job deleted.")
            else:
                print("Job not found.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
