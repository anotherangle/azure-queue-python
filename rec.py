from azure.storage.queue import QueueClient

queue = QueueClient.from_connection_string(conn_str="your_connection_string", queue_name="your_queue_name")
response = queue.receive_messages()

for message in response:
    print(message.content)
    queue.delete_message(message)
