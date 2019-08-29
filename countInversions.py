# We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.
# The number of inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].
# Return the Number of inversions


def countInversionsGlobal(A):

    def mergeAndCountInversions(arr1, arr2):

        output = []
        c = 0

        i = 0
        j = 0

        while i < len(arr1) and j < len(arr2):

            if arr1[i] == arr2[j]:
                output.append(arr1[i])
                output.append(arr2[j])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                output.append(arr1[i])
                i += 1
            else:  # arr1[i] > arr2[j]:
                output.append(arr2[j])
                j += 1
                # number of inversions at index j is the number of remaining elements of arr1
                c += len(arr1) - i

        while(i < len(arr1)):
            output.append(arr1[i])
            i += 1

        while(j < len(arr2)):
            output.append(arr2[j])
            j += 1

        return c, output

    # BC
    if not A or len(A) == 1:
        return 0, A

    inversions = 0
    # get number of inversions from halfs
    inversions1, sortedArr1 = countInversionsGlobal(A[:len(A)//2])
    inversions2, sortedArr2 = countInversionsGlobal(A[len(A)//2:])

    inversions += inversions1
    inversions += inversions2

    inversionsMerge, sortedArr = mergeAndCountInversions(
        sortedArr1, sortedArr2)

    inversions += inversionsMerge

    return inversions, sortedArr


f = open("InversionInput.txt", "r")

arr = []
for line in f:
    n = int(line)
    arr.append(n)

print(countInversionsGlobal(arr)[0])
