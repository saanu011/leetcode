// link: https://leetcode.com/problems/lru-cache/description/


import (
	"container/list"
)

type LRUCache struct {
	list     list.List
	capacity int
}

func Constructor(capacity int) LRUCache {
	return LRUCache{
		capacity: capacity,
		list:     list.List{},
	}
}

func (this *LRUCache) Get(key int) int {
	for e := this.list.Front(); e != nil; e = e.Next() {
		// ss := []byte(e.Value)
		// var i []int

		// _ = json.Decode(ss, i)
		i := e.Value.([]int)
            // fmt.Println("asdfsad", i[0])
		if i[0] == key {
			this.list.Remove(e)
			this.list.PushFront([]int{i[0], i[1]})
			return i[1]
		}
	}
	return -1
}

func (this *LRUCache) Put(key int, value int) {
	val := []int{key, value}
	for e := this.list.Front(); e != nil; e = e.Next() {
		i := e.Value.([]int)
        // fmt.Println(i[0])
		if i[0] == key {
			this.list.Remove(e)
			this.list.PushFront(val)
			return
		}
	}
    // fmt.Println(key, "key")
	this.list.PushFront(val)
    if this.list.Len() > this.capacity {
	    this.list.Remove(this.list.Back())
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */