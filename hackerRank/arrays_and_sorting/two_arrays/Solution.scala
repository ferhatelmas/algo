package arrays_and_sorting.two_arrays

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    val l = Source.stdin.getLines
    var n = l.next.toInt
    while(n > 0) {
      val List(_, k) = l.next.split("\\s").map(_.toInt).toList
      val a = l.next.split("\\s").map(_.toInt).toArray.sorted
      val b = l.next.split("\\s").map(_.toInt).toArray.sorted(Ordering[Int].reverse)
      println(if(a.zip(b).filterNot(t => t._1 + t._2 >= k).length == 0) "YES" else "NO")
      n -= 1
    }
  }
}
