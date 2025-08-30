try:
    print(2//0)
except Exception as e:
    print(e)
finally:
    print("This is finally block")