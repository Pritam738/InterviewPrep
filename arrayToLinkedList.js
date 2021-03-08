function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
 }
function createL(a){
    let node, temp;
    for(let i=a.length-1; i >= 0; i--){
        if(!node)
            node = new ListNode(a[i]);
        else {
            temp = new ListNode(a[i]);
            temp.next = node;
            node = temp;
        }
    }
    return node;
}
