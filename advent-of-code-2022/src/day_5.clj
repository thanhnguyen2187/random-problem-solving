(ns day-5
  (:require [clojure.string :as str]))

(defn to-ints
  [seq]
  (map #(Integer/parseInt %) seq))

(defn apply-action
  [stacks action]
  (let [[amount from to] action
        from-stack (get stacks from)
        to-stack (get stacks to)
        items (take-last amount from-stack)
        new-from-stack (drop-last amount from-stack)
        new-to-stack (concat to-stack (reverse items))]
    (-> stacks
        (assoc from new-from-stack)
        (assoc to new-to-stack)
        )))

(defn apply-action-2
  [stacks action]
  (let [[amount from to] action
        from-stack (get stacks from)
        to-stack (get stacks to)
        items (take-last amount from-stack)
        new-from-stack (drop-last amount from-stack)
        new-to-stack (concat to-stack items)]
    (-> stacks
        (assoc from new-from-stack)
        (assoc to new-to-stack)
        )))

(apply-action
  {1 ["A" "B"]
   2 ["C"]}
  [2 1 2])

;; part 1
(let [stacks (->> (slurp "inputs/day_5_transformed_1.txt")
                  (str/trim-newline)
                  (str/split-lines)
                  (map #(str/split % #" "))
                  (zipmap (range))
                  (#(update-keys % inc))
                  (#(update-vals % reverse))
                  )
      actions (->> (slurp "inputs/day_5_transformed_2.txt")
                   (str/trim-newline)
                   (str/split-lines)
                   (map #(str/split % #"  "))
                   (map to-ints)
                   (into [])
                   )]
  ;;(into (sorted-map) stacks)
  (->> actions
       (reduce apply-action stacks)
       (into (sorted-map))
       (vals)
       (map last)
       (str/join "")))

;; part 2
(let [stacks (->> (slurp "inputs/day_5_transformed_1.txt")
                  (str/trim-newline)
                  (str/split-lines)
                  (map #(str/split % #" "))
                  (zipmap (range))
                  (#(update-keys % inc))
                  (#(update-vals % reverse))
                  )
      actions (->> (slurp "inputs/day_5_transformed_2.txt")
                   (str/trim-newline)
                   (str/split-lines)
                   (map #(str/split % #"  "))
                   (map to-ints)
                   (into [])
                   )]
  ;;(into (sorted-map) stacks)
  (->> actions
       (reduce apply-action-2 stacks)
       (into (sorted-map))
       (vals)
       (map last)
       (str/join "")))

