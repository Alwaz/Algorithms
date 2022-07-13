

//Bubble Sort 
class Bubble_Sort {



	       //method for printing array
	public static void print_array(int[] arr) {

		for(int i : arr) 
			System.out.print(i+" ");
	} 
  

  public static void bubbleSort(int[] arr) {

     //compare two elements then swap em
  	for(int i=0 ; i<arr.length;i++){
  		for(int j=0 ; j<arr.length-1 ; j++){
  			if(arr[j+1]<arr[j]){
  			  int temp=arr[j];
  			 arr[j]=arr[j+1];
  			 arr[j+1]=temp;
  			}
  		}
  	}
  }


	public static void main(String[] args) {

		int[] arr={5,3,8,13,9};
		System.out.print("Unsorted array : ");
		print_array(arr);
		System.out.print("\n");
		System.out.print("Sorted array : ");
		bubbleSort(arr);
		print_array(arr);


		
	}
}