(ns day-3
  (:require [clojure.core.match :refer [match]]
            [clojure.string :as str]
            [clojure.set :as set]))

(defn split-half
  [text]
  (let [length (count text)
        middle-index (/ length 2)]
    [(subs text 0 middle-index)
     (subs text middle-index)]))

(defn find-common-characters
  [text-1 text-2]
  (let [text-1-characters (apply hash-set (seq text-1))
        text-2-characters (apply hash-set (seq text-2))]
    (set/intersection text-1-characters text-2-characters)))

(defn calculate-character-score
  [character]
  (let [ascii-number (int character)]
    (cond (and (<= 65 ascii-number)
               (<= ascii-number 90)) (-> ascii-number
                                         (- 64)
                                         (+ 26))
          (and (<= 97 ascii-number)
               (<= ascii-number 122)) (-> ascii-number
                                          (- 96))
          :else (throw (ex-info "day-3.calculate-character-score unreachable path"
                                {:character character}))
          )))

;; part 1
(->> (slurp "inputs/day_3.txt")
     (str/trim-newline)
     (str/split-lines)
     (map split-half)
     (map (fn [[text-1 text-2]]
            (find-common-characters text-1 text-2))
          )
     (map (fn [characters]
            (->> characters
                 (map calculate-character-score)
                 (reduce +))))
     (reduce +))

;; part 2
(->> (slurp "inputs/day_3.txt")
     (str/trim-newline)
     (str/split-lines)
     (partition 3)
     (map #(reduce find-common-characters %))
     (map (fn [characters]
            (->> characters
                 (map calculate-character-score)
                 (reduce +))))
     (reduce +))
