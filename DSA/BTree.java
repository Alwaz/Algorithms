

//Creating a Binary Tree



class BTree {

	Object root;
	BTree left;
	BTree right;

	public BTree(Object root) {

		this.root=root;
	}

	public BTree(Object root , BTree left , BTree right) {

        this.root=root;
		this.right=right;
		this.left=left;
	}

       //getter methods
	public Object getRoot() {

		Object oldroot=this.root;
		this.root=root;
		return oldroot;
	}

	public Object getLeft() {

		Object oldleft=this.left;
		this.left=left;
		return oldleft;
	}

	public Object getRight() {
         
         Object oldright=this.right;
         this.right=right;
         return oldright;
	}

      //setter methods
	public Object setRoot(Object root) {
             
        Object old_root=this.root;
		this.root=root;
		return old_root;

	}

	public BTree setLeft(BTree left) {

		BTree old_left=this.left;
		this.left=left;
		return old_left;
	}

	public BTree setRight(BTree right) {

	 	 BTree old_right=this.right;
         this.right=right;
         return old_right;
	}



	public boolean isleaf() {

		if(left==null && right==null) return true;
		else return false;
	}


	public int size() {

     if(left == null && right == null) 
     	{return 1;}
     else if(right==null) {return 1+left.size();}
	 else if(left==null) {return 1+right.size();}
	 return 1+left.size()+right.size(); //recursion calling size method inside size method.
	}

	public  String  toString() {

		StringBuffer sb=new StringBuffer(" ");    // for inorder = left root right 
		if(left!=null) sb.append(left.toString()+ ",");
		sb.append(root);
		if(right!=null) sb.append("," +right);
		return sb+" ";
	}

	public String postOrder() { //for post Order = left right root

		StringBuffer bf=new StringBuffer("");
		if(left!=null) bf.append(","+left.toString());
		if(right!=null) bf.append(right.toString()+","); //a lil prob here
		bf.append(root);
		return bf+" ";
	}

    public String preOrder() { //for pre Order = root left right

		StringBuffer bf=new StringBuffer(" ");
		bf.append(root);
		if(left!=null) bf.append(left.toString()+",");
		if(right!=null) bf.append(right.toString()+",");
		return bf+"";
  }


   //convert left subtree to array
  public Object[] toArray() {
  	System.out.print("toArray for Left Sub Tree: ");

     Object[] arr=new Object[left.size()];
     for(int i=0 ; i<left.size() ; i++) {
     	arr[i]=getLeft();
     	System.out.print(arr[i]);
     }

   return arr;
  }


   public static void main(String[] args) {
   	//Object[] obj=new Object[100];
   	
   	BTree bt1=new BTree("A");
   	BTree bt2=new BTree("B");
   	BTree bt3=new BTree("C");
   	BTree bt4=new BTree("D");
   	BTree bt5=new BTree("E");

   bt1.setRoot("A");
   	bt1.setLeft(bt2);
   	bt1.setRight(bt3);
   	bt2.setLeft(bt4);
   	bt2.setRight(bt5);


   	/*System.out.print(bt1.getRoot());
,   	System.out.print(bt1.getLeft());
   	System.out.print(bt1.getRight());
   	System.out.print(bt2.getLeft());
   	System.out.print(bt2.getRight());*/

   	System.out.print("In Order Tree: "+bt1.toString());
   	System.out.print("\n");
   	System.out.print("Post Order Tree: "+bt1.postOrder());
   	System.out.print("\n");
   	System.out.print("Pre Order Tree: "+bt1.preOrder());
   	System.out.print("\n");
   	System.out.println(bt1.toArray());














   }


}