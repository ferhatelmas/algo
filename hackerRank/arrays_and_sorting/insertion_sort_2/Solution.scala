package arrays_and_sorting.insertion_sort_2

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    val l = Source.stdin.getLines
    val v = l.next.toInt
    val ls = l.next.split("\\s").map(_.toInt).toArray
    (1 to v-1).foreach(i => {
      val k = ls(i)
      var j = i
      while(j > 0 && ls(j-1) > k) {
        ls(j) = ls(j-1)
        j -= 1
      }
      ls(j) = k
      println(ls.mkString(" "))
    })
  }
}
