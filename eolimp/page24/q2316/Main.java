package page24.q2316;

import java.util.Scanner;

public class Main {

  static class Node {
    Node left, right;
    int data;

    public Node(int data) {
      left = null;
      right = null;
      this.data = data;
    }
  }

  static class BST {
    Node root = null;
    boolean flag = false;

    public void add(int data) {
      if(root == null) root = new Node(data);
      else if(root.data != data) add(root, data);
    }

    private void add(Node n, int data) {
      if(n.data > data)
        if(n.left == null) n.left = new Node(data);
        else add(n.left, data);
      else if(n.data < data)
        if(n.right == null) n.right = new Node(data);
        else add(n.right, data);
    }

    public StringBuilder traverseLeaves() {
      return traverse(root, new StringBuilder());
    }

    private StringBuilder traverse(Node n, StringBuilder sb) {
      if(n == null) return sb;
      if(n.left == null && n.right == null) {
        sb.append(n.data);
        sb.append(" ");
      }
      sb = traverse(n.left, sb);
      sb = traverse(n.right, sb);
      return sb;
    }
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    BST bst = new BST();int n;
    while((n=in.nextInt()) != 0) {
      bst.add(n);
    }
    StringBuilder sb = bst.traverseLeaves();
    if(sb.length() > 0) sb.delete(sb.length()-1, sb.length());
    System.out.println(sb.toString());
  }

}

