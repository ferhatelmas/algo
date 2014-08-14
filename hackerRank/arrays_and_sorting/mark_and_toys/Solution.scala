package arrays_and_sorting.mark_and_toys

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    val l = Source.stdin.getLines
    val List(n, k) = l.next.split("\\s").map(_.toInt).toList
    val ls = l.next.split("\\s").map(_.toInt).toArray.sorted
    var i, sum = 0
    while(i < ls.length && sum + ls(i) < k) {
      sum += ls(i)
      i += 1
    }
    println(i)
  }
}
