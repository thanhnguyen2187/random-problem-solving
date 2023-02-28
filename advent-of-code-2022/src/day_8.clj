(ns day-8
  (:require [clojure.string :as str]
            [clojure.core.match :refer [match]]
            [clojure.math.combinatorics :as combo]))

(defn get-top-positions
  [x y x-length y-length]
  (->> (range (inc y) y-length)
       (map (fn [y] [x y]))))

(defn get-bottom-positions
  [x y x-length y-length]
  (->> (range 0 y)
       (reverse)
       (map (fn [y] [x y]))))

(defn get-left-positions
  [x y x-length y-length]
  (->> (range 0 x)
       (reverse)
       (map (fn [x] [x y]))))

(defn get-right-positions
  [x y x-length y-length]
  (->> (range (inc x) x-length)
       (map (fn [x] [x y]))))

(defn is-visible
  [input-map x y x-length y-length]
  (let [get-value (fn [[x y]] (get-in input-map [y x] 0))
        value (get-value [x y])
        left-positions (get-left-positions x y x-length y-length)
        right-positions (get-right-positions x y x-length y-length)
        top-positions (get-top-positions x y x-length y-length)
        bottom-positions (get-bottom-positions x y x-length y-length)
        left-values (map get-value left-positions)
        right-values (map get-value right-positions)
        top-values (map get-value top-positions)
        bottom-values (map get-value bottom-positions)]
    ;; check if `value` is maximal within the four directions
    ;; using `reduce` to ensure that `max` returns `-1` in case there is no value
    (or (> value (reduce max -1 left-values))
        (> value (reduce max -1 right-values))
        (> value (reduce max -1 top-values))
        (> value (reduce max -1 bottom-values))
        )
    ))

(defn calculate-scenic-score-by-values
  [value direction-values]
  (+ (->> direction-values
          (take-while (fn [direction-value]
                        (< direction-value value)))
          (count))
     (->> direction-values
          (filter (fn [direction-value]
                    (>= direction-value value)))
          (first)
          (conj [])
          (remove nil?)
          (count))
     ))

(defn calculate-scenic-score
  [input-map x y x-length y-length]
  (let [get-value (fn [[x y]] (get-in input-map [y x] 0))
        value (get-value [x y])
        calculate-score (fn [direction-values] (calculate-scenic-score-by-values value direction-values))
        left-positions (get-left-positions x y x-length y-length)
        right-positions (get-right-positions x y x-length y-length)
        top-positions (get-top-positions x y x-length y-length)
        bottom-positions (get-bottom-positions x y x-length y-length)
        left-values (map get-value left-positions)
        right-values (map get-value right-positions)
        top-values (map get-value top-positions)
        bottom-values (map get-value bottom-positions)
        left-score (calculate-score left-values)
        right-score (calculate-score right-values)
        top-score (calculate-score top-values)
        bottom-score (calculate-score bottom-values)]
    (* left-score right-score top-score bottom-score)
    ))

(calculate-scenic-score
  [[3 0 3 7 3]
   [2 5 5 1 2]
   [6 5 3 3 2]
   [3 3 5 4 9]
   [3 5 3 9 0]
   ]
  1 2
  5 5)

(let [input-map (->> (slurp "inputs/day_8.txt")
                     (str/trim-newline)
                     (str/split-lines)
                     (map seq)
                     (map (fn [chars] (map int chars)))
                     (to-array-2d)
                     )
      y-length (alength input-map)
      x-length (alength (aget input-map 0))
      positions (combo/cartesian-product (range y-length)
                                         (range x-length))
      visible-positions (filter (fn [[x y]]
                                  (is-visible input-map
                                              x y
                                              x-length y-length))
                                positions)
      part-1-answer (count visible-positions)
      part-2-answer (->> positions
                         (map (fn [[x y]]
                                (calculate-scenic-score input-map
                                                        x y
                                                        x-length y-length)))
                         (apply max))]
  {:part-1-answer part-1-answer
   :part-2-answer part-2-answer
   })
