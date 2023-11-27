class Hello:
    def __init__(self, name) -> None:
        self.name = name
        
    def say_hello(self):
        print("Hello " + self.name)
        
    def whats_my_name(self):
        return self.name
    
def main():
    john = Hello("john")
    john.say_hello()
    
if __name__ == "__main__":
    main()