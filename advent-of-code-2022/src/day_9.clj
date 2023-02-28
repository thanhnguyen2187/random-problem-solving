(ns day-9
  (:require [clojure.string :as str]
            [clojure.core.match :refer [match]])
  )

(defn move-knot
  [[x y] direction]
  (match direction
         :overlapped [x y]
         :up [x (inc y)]
         :down [x (dec y)]
         :left [(dec x) y]
         :right [(inc x) y]
         :left-down [(dec x) (dec y)]
         :left-up [(dec x) (inc y)]
         :right-down [(inc x) (dec y)]
         :right-up [(inc x) (inc y)]
         :else (throw (ex-info (str "day-9.move-knot unreachable path " direction)
                               {:direction direction}))))

(defn character-to-direction
  [character]
  (match character
         "U" :up
         "D" :down
         "L" :left
         "R" :right))

(defn line-to-directions
  [line]
  (-> line
      (str/split #" ")
      ((fn [[character time-str]]
         (repeat (Integer/parseInt time-str)
                 (character-to-direction character))
         ))
      ))

(defn calculate-direction
  "Calculate the relative position of `head` comparing to `tail`."
  [tail head]
  (let [[tail-x tail-y] tail
        [head-x head-y] head
        compare-x (compare tail-x head-x)
        compare-y (compare tail-y head-y)]
    (match
      [compare-x compare-y]
      [0 0] :overlapped

      [1 0] :left
      [-1 0] :right
      [0 -1] :up
      [0 1] :down

      [1 1] :left-down
      [1 -1] :left-up
      [-1 1] :right-down
      [-1 -1] :right-up

      :else (throw (ex-info "day-9.calculate-relative-position unreachable path"
                            {:tail tail
                             :head head})))))

(defn calculate-distance
  [tail head]
  (let [[tail-x tail-y] tail
        [head-x head-y] head]
    (+ (abs (- head-x tail-x))
       (abs (- head-y tail-y)))))

(defn advance-tail
  [tail head]
  (let [relative-direction (calculate-direction tail head)
        distance (calculate-distance tail head)
        new-tail (move-knot tail relative-direction)]
    (match [relative-direction distance]
           [:overlapped _] tail
           [(:or :left :right :up :down) 1] tail
           [(:or :left-down :left-up :right-down :right-up) 2] tail
           [(:or :left :right :up :down) 2] new-tail
           [(:or :left-down :left-up :right-down :right-up) (:or 3 4)] new-tail
           :else (throw (ex-info (str "day-9.advance-tail unreachable path " {:tail tail :head head})
                                 {:tail tail :head head})))))

(defn advance-state
  [state head-direction]
  (let [{head :head
         tail :tail} state
        new-head (move-knot head head-direction)
        new-tail (advance-tail tail new-head)]
    {:head new-head
     :tail new-tail}))

(defn advance-state-2
  [state head-direction]
  (let [{head  :head
         tails :tails} state
        new-head (move-knot head head-direction)
        new-tails (reduce (fn [result new-tail]
                            (conj result
                                  (advance-tail new-tail
                                                (last result))))
                          [new-head]
                          tails)
        new-state {:head  new-head
                   :tails (drop 1 new-tails)}]
    new-state))

(try
  (let [directions (->> (slurp "inputs/day_9.txt")
                        (str/trim-newline)
                        (str/split-lines)
                        (map line-to-directions)
                        (reduce concat []))
        initial-state {:head [0 0]
                       :tail [0 0]}
        states (reductions advance-state initial-state directions)
        part-1-answer (->> states
                           (map :tail)
                           (distinct)
                           (count))
        initial-state-2 {:head  [0 0]
                         :tails (repeat 9 [0 0])}
        states-2 (reductions advance-state-2 initial-state-2 directions)
        part-2-answer (->> states-2
                           (map :tails)
                           (map last)
                           (distinct)
                           (count))
        ]
    [part-1-answer
     part-2-answer]
    )
  (catch Exception ex
    (println ex)))

