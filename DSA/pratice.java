

//Quick Sort

class QuickSortMiddle {

          //partition method
	public int partition(int[] arr , int low , int high) {


          //taking middle element as pivot element
		int pivot=arr[(low+high)/2];

		while(low<=high) {
			while(arr[low]<pivot) {
				low++;
			}
			while(arr[high]>pivot){
				high--;
			}
			if(low<=high){
			    //swaping   
				int temp;
				temp=arr[low];
				arr[low]=arr[high];
				arr[high]=temp;

				low++;
				high--;
			}
		
		}
		return low;
	}	//end of partition


     //for recursion of partition
  void quicksort_recursion(int[] arr , int low , int high){
  	int pi=partition(arr,low,high);
  	if(low<pi-1)
  		quicksort_recursion(arr , low , pi-1);
  	if(pi<high)
  		quicksort_recursion(arr , pi , high);

  }





          //method for printing array
	public void print_array(int[] arr) {

		for(int i : arr) 
			System.out.print(i+" ");
	} 


	public static void main(String[] args) {

		QuickSortMiddle q=new QuickSortMiddle();
		int[] arr={5,2,16,3,8,7,15};
		int size=arr.length;

	     System.out.print("Unsorted array : ");
		q.print_array(arr);


        System.out.println("\n");
        System.out.print("Sorted array : ");
		q.quicksort_recursion(arr,0,size-1);
		q.print_array(arr);


	}
}