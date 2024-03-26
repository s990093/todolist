from faker import Faker


from faker import Faker

def get_faker_tasks(num_tasks=20):
    faker = Faker()
    tasks = []
    for _ in range(num_tasks):
        task_name = faker.catch_phrase()
        completed = faker.random_element(elements=(0, 1))
        task_type = faker.word()
        tasks.append({
            "name": task_name,
            "completed": completed,
            "type": task_type
        })
    return tasks

