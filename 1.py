public class SortingAlgorithms {

    // 冒泡排序方法
    public static int[] bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // 交换 arr[j] 和 arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
        return arr;
    }

    public static void main(String[] args) {
        int[] nums1 = {5, 2, 3, 1};
        int[] sortedNums1 = bubbleSort(nums1);
        for (int num : sortedNums1) {
            System.out.print(num + " ");
        }
        System.out.println();

        int[] nums2 = {5, 1, 1, 2, 0, 0};
        int[] sortedNums2 = bubbleSort(nums2);
        for (int num : sortedNums2) {
            System.out.print(num + " ");
        }
    }
}