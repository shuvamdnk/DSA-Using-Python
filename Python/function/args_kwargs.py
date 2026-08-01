def student_details(name, *skill, **certificates):
    print(name)
    print(skill)
    print(certificates)


student_details("Shuvam", "node","python","php",udemy="Node js",coursea="Python")