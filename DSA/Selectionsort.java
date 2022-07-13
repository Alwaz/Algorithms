class SelectionSort {

	public static void printArray(int[] arr) {

		for(int i : arr){
			System.out.print(i+" ");
		}
	}

	public static void main(String[] args) {
		
		int[] arr={50,20,34,5,6,1};
		System.out.println("Unsorted Array : ");
		printArray(arr);


             //Selection Sort

		int min,temp=0;
		for(int i=0 ; i<arr.length ; i++){

                  min=i;

			for(int j=i+1 ; j<arr.length ; j++)
			{
				if(arr[j]<arr[min]){
					min=j;
				}

			}
			temp=arr[i];
			arr[i]=arr[min];
			arr[min]=temp;

		}
		    System.out.println("\n");
		    System.out.println("Sorted Array : ");
			printArray(arr);


   } 
} //end of class		