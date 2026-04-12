n, m, k = map(int, input().split())
package_sizes = sorted(map(int, input().split()), reverse=True)
max_percentage = sum(package_sizes[:m+k])/sum(package_sizes)*100

if max_percentage == int(max_percentage):
    print(int(max_percentage))
else:
    print("{:.9f}".format(max_percentage))
