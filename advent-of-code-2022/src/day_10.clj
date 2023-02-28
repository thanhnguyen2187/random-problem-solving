(ns day-10
  (:require [clojure.string :as str]
            [clojure.core.match :refer [match]]
            [instaparse.core :as insta]))

(def sample-state
  {:X     1
   :cycle 1})

(def sample-instruction
  {:name "addx"
   :V    3})

(defn line-to-instruction
  [index line]
  (let [parts (str/split line #" ")
        result {:cycle index}]
    (match parts
           ["noop"] (assoc result :name "noop")
           ["addx" V] (assoc result :name "addx" :V (Integer/parseInt V))
           :else (throw (ex-info (str "day-10.line-to-instruction unreachable path " {:index index :line line})
                                 {:index index :line line})))))

(defn advance-state
  [state instruction]
  (let [instruction-name (instruction :name)]
    (case instruction-name
      "noop" (update state :cycle inc)
      "addx" (-> state
                 (update :X + (instruction :V))
                 (update :cycle + 2)))))

(advance-state sample-state
               {:name "noop"})

(defn fill-missing-states
  [states]
  (reduce (fn [filled-states state]
            (let [last-state (last filled-states)
                  last-cycle (last-state :cycle)
                  current-cycle (state :cycle)
                  missing-cycles (range (inc last-cycle)
                                        current-cycle)
                  missing-states (map (fn [missing-cycle]
                                        (assoc last-state :cycle missing-cycle))
                                      missing-cycles)]
              (as-> filled-states _
                    (concat _ missing-states)
                    (into [] _)
                    (conj _ state))))
          [(first states)]
          (drop 1 states))
  )

(defn state-to-character
  [state]
  (let [X (state :X)
        cycle (-> state
                  (:cycle)
                  (mod 40))]
    (if (<= (dec X) (dec cycle) (inc X))
      "██"
      "  ")))

(let [instructions (->> (slurp "inputs/day_10.txt")
                        (str/trim-newline)
                        (str/split-lines)
                        (map line-to-instruction (range 1 ##Inf))
                        )
      initial-state {:cycle 1
                     :X     1}
      ;;states (reductions advance-state initial-state instructions)
      states (->> instructions
                  (reductions advance-state initial-state)
                  (into [])
                  (fill-missing-states))
      part-1-result (->> states
                         (filter (fn [state]
                                   (-> state
                                       (:cycle)
                                       (mod 40)
                                       (= 20))))
                         (map (fn [state]
                                (* (state :X)
                                   (state :cycle))))
                         (reduce +))
      part-2-result (->> states
                         (map state-to-character)
                         (partition 40)
                         (map (fn [characters]
                                (str/join "" characters)))
                         )
      ]
  ;;instructions
  ;;states
  ;;actions
  [part-1-result
   part-2-result]
  )
