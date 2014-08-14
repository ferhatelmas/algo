package arrays_and_sorting.insertion_sort_1

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    val l = Source.stdin.getLines
    val v = l.next.toInt
    val ls = l.next.split("\\s").map(_.toInt).toArray
    var (k, i) = (ls(v-1), v-1)
    while(i > 0 && ls(i-1) > k) {
      ls(i) = ls(i-1)
      i -= 1
      println(ls.mkString(" "))
    }
    ls(i) = k
    println(ls.mkString(" "))
  }
}
