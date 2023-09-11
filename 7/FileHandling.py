def save_call(callback):
    def inner_func(*args, **kwargs):
        try:
            return callback(*args, **kwargs)
        except Exception as e:
            print(f"{type(e)}: {e}")
    
    return inner_func


class FileHandling:
    @save_call
    def append_data(self, path: str, data:str):
        with open(path, mode='a', encoding='utf-8') as f:
            f.write(data)
    
    @save_call
    def get_data(self, path):
        with open(path, 'r', encoding='utf8') as f:
            return f.read()


file_service = FileHandling()
file_service.append_data('7/new_file.txt', '💤2 пример\n')
content = file_service.get_data('7/new_file.txt')
print(content)


# print(ord('к'))