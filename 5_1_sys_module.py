import sys
print(sys.argv)

sys.stdout=open('f','w')
print('salam')

print(sys.builtin_module_names)
print(sys.executable)
print(sys.getsizeof(str))
sys.exit(10)
