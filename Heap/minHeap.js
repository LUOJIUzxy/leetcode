
class MinHeap{
    constructor(heapSize){
        this.heapSize = heapSize;
        this.minHeap = new Array(heapSize + 1).fill(0);;
        this.minHeap[0] = -1;
        // realSize records the number of elements in the Heap
        this.realSize = 0;
    }

    add(element){
        this.realSize++;
        if (this.realSize > this.heapSize){
            console.log("Healp is full, added too many elements!");
            this.realSize--;
            return;
        }

        //first add it to the tail of the array
        this.minHeap[this.realSize] = element;

        let index = this.realSize;
        let parent = Math.floor(index / 2);
        while( this.minHeap[parent] > this.minHeap[index] && index > 1 ){
            let temp = this.minHeap[parent];
            this.minHeap[parent] = this.minHeap[index] 
            this.minHeap[index] = temp;

            index = parent;
            parent = Math.floor(index / 2);
        }
    }
    //Top Element of the heap
    top(){
        return this.minHeap[1];
    }

    //Pop the top element of the min Heap
    pop(){
        if (this.realSize < 1){
            console.log("there's no element left!");
            return null;
        }

        const removedElement = this.minHeap[1];
        this.minHeap[1] = this.minHeap[this.realSize];
        this.realSize--;

        let index = 1;
        let left = index * 2;
        let right = index * 2 + 1;
        while(index <= Math.floor(this.realSize/2)){
            if( this.minHeap[index] > this.minHeap[left] || this.minHeap[index] > this.minHeap[right]){
                if (this.minHeap[left] >= this.minHeap[right]){
                    let temp = this.minHeap[left];
                    this.minHeap[left] = this.minHeap[index];
                    this.minHeap[index] = temp;

                    index = left;
                    left = index * 2;
                } else {
                    let temp = this.minHeap[right];
                    this.minHeap[right] = this.minHeap[index];
                    this.minHeap[index] = temp;

                    index = right;
                    right = index * 2 + 1;
                }
            } else {
                break;
            }
        }
        return removedElement;
    }

    size() {
        return this.realSize;
    }

     toString() {
        return `[${this.minheap.slice(1, this.realSize + 1).join(', ')}]`;
    }


}

const minHeap = new MinHeap(5);
minHeap.add(3);
minHeap.add(1);
minHeap.add(2);
console.log(minHeap); // [1, 3, 2]
console.log(minHeap.top()); // 1
console.log(minHeap.pop()); // 1
console.log(minHeap.pop()); // 2
console.log(minHeap.pop()); // 3
minHeap.add(4);
minHeap.add(5);
console.log(minHeap); // [4, 5]