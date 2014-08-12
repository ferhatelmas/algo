package warmup.game_of_thrones_1

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    val i = Source.stdin.getLines.next.sorted.groupBy(c => c).map({ case (k, s) => s.length%2 }).sum
    println(if(i < 2) "YES" else "NO")
  }
}
