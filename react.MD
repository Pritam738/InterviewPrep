# What is React?
React is a JavaScript library for building user interfaces. It is developed by Facebook.

# What are React’s Key Features?
1)Virtual DOM

2)JSX

3)Unidirectional Data Flow

4)Server-Side Rendering

# What is JSX?
JSX is a Javascript syntax extension that allows us to write HTML in our JavaScript to create React Elements

Babel compiles JSX into React.createElement() calls

Cleaner code with JSX expressions

Safer code as the usage of JSX prevents XSS attacks


# What is the Virtual DOM?
Manipulating the actual DOM is expensive

Virtual DOM: React makes a virtual representation of the actual DOM in memory

Expected changes are first reflected in an updated version of the Virtual DOM. The updated virtual DOM is compared with its previous version using React’s 

‘diffing’ algorithm to determine how to best update the real DOM

# Reconciliation
React provides a declarative API so that you don’t have to worry about exactly what changes on every update. This makes writing applications a lot easier, but it might not be obvious how this is implemented within React.

When you use React, at a single point in time you can think of the render() function as creating a tree of React elements. On the next state or props update, that render() function will return a different tree of React elements. React then needs to figure out how to efficiently update the UI to match the most recent tree.

There are some generic solutions to this algorithmic problem of generating the minimum number of operations to transform one tree into another. However, the state of the art algorithms have a complexity in the order of O(n3) where n is the number of elements in the tree.

If we used this in React, displaying 1000 elements would require in the order of one billion comparisons. This is far too expensive. Instead, React implements a heuristic O(n) algorithm based on two assumptions:

Two elements of different types will produce different trees.
The developer can hint at which child elements may be stable across different renders with a key prop.

## The Diffing Algorithm

When diffing two trees, React first compares the two root elements. The behavior is different depending on the types of the root elements.

### Elements Of Different Types
Whenever the root elements have different types, React will tear down the old tree and build the new tree from scratch. Going from <a> to <img>, or from <Article> to <Comment>, or from <Button> to <div> - any of those will lead to a full rebuild.

When tearing down a tree, old DOM nodes are destroyed. Component instances receive componentWillUnmount(). When building up a new tree, new DOM nodes are inserted into the DOM. Component instances receive componentWillMount() and then componentDidMount(). Any state associated with the old tree is lost.

Any components below the root will also get unmounted and have their state destroyed. For example, when diffing:

```
<div>
  <Counter />
</div>

<span>
  <Counter />
</span>
```

This will destroy the old Counter and remount a new one.

### DOM Elements Of The Same Type
When comparing two React DOM elements of the same type, React looks at the attributes of both, keeps the same underlying DOM node, and only updates the changed attributes. For example:

```
<div className="before" title="stuff" />

<div className="after" title="stuff" />
```

By comparing these two elements, React knows to only modify the className on the underlying DOM node.

When updating style, React also knows to update only the properties that changed. For example:

```
<div style={{color: 'red', fontWeight: 'bold'}} />

<div style={{color: 'green', fontWeight: 'bold'}} />
```

When converting between these two elements, React knows to only modify the color style, not the fontWeight.

After handling the DOM node, React then recurses on the children.


When a component updates, React updates the props of the underlying component instance to match the new element, and calls componentWillReceiveProps() and componentWillUpdate() 

Next, the render() method is called and the diff algorithm recurses on the previous result and the new result.



# What is a Component in React and what are the two main ways to define them?
Component is an independent reusable piece of the UI
React needs to create an instance in case of Class Component, while it doesn’t do that for a functional component. 
Class Component: Component implemented using ES6 Classes extending React.Component
Function Component: Component implemented by a JS function that takes a props argument and returns a React element

## class component
```
class ClickCounter extends React.Component {
    constructor(props) {
        super(props);
        this.state = {count: 0};
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick() {
        this.setState((state) => {
            return {count: state.count + 1};
        });
    }


    render() {
        return [
            <button key="1" onClick={this.handleClick}>Update counter</button>,
            <span key="2">{this.state.count}</span>
        ]
    }
}
```
## function component

```
const ExampleComponent = (props) => {
    return ( <h1>Welcome to Educative!</h1>);
}
        
export default class App extends React.Component {
  render() {
    //rendering ExampleComponent component in App Component
    return (
      <div>
        <ExampleComponent/> 
        </div>
    );
  }
}
```

# How do Class components compare with Function components?
With React Hooks, class components are replaceable with function components for the majority of use cases
In the past, stateful and life cycle logic could only be incorporated in class components

# Function Component Disadvantages
There are no Hook equivalents yet for the uncommon life cycles: getSnapshotBeforeUpdate and componentDidCatch
Older third-party libraries might not be compatible with hooks yet

# Class Components Disadvantages
Classes add unnecessary confusion for the sake of syntactic sugar²
Classes lead to a bulky hierarchy tree, especially during code reuse, which results in performance decreases and difficulty testing³
Class lifecycle methods split up related pieces of code

# What are props and state in React?
props is the JavaScript object, passed into a Component, that holds the configuration properties¹
props is immutable by the receiving Component
state is the JavaScript object, managed within the Component, that holds its internal state.
Updates to either trigger a re-render

# What causes a component to update?
A re-render of the parent which may entail new Props
setState()
(B) forceUpdate() (and that it should be avoided!)


# What doessetState() do and how does it work?
setState() schedules an update to a component’s state object. When state changes, the component responds by re-rendering.
Calls to setState() are asynchronous and may be batched
Updates to this.state do not reflect the new value immediately after calling setState()
Because of its asynchronous nature, Calling setState() by passing an object containing the current state value can result in unexpected behaviour
Passing setState() a function rather than an object allows you to access the current state value, avoiding potential unexpected behaviour caused asynchronicity
```
incrementCount() {
  this.setState((state) => {
    // Important: read `state` instead of `this.state` when updating.
    return {count: state.count + 1}
  });
}

handleSomething() {
  // Let's say `this.state.count` starts at 0.
  this.incrementCount();
  this.incrementCount();
  this.incrementCount();
  // If you read `this.state.count` now, it would still be 0.
  // But when React re-renders the component, it will be 3.
}
```

# walk me through the main phases of the React Lifecycle
3 phases: Mounting, Updating, Unmounting
Mounting: constructor → render → DOM update → componentDidMount
Updating: render → DOM update → componentDidUpdate
Unmounting: componentWillUnmount
(B) inclusion of getDerivedStateFromPropsand shouldComponentUpdate


# How can I prevent unnecessary re-rendering?
React.PureComponent : Components created off of this class do a shallow comparison with the upcoming props and state and re-render if there are changes
React.Memo: Higher-order component that works like React.PureComponent but used for function components
shouldComponentUpdate : Lifecycle method that takes in the next props and state and returns a boolean indicating if the component should rerender

# What are refs and what are they used for?
Refs provide access to DOM nodes or React elements created in the render() method
In the past, refs were limited only to class components but now can be accessed in function components via the useRef hook
Uses include:
Managing focus, text selection, or media playback.
Triggering imperative animations.
Integration with third-party DOM libraries.

# When rendering lists, what are keys and why do you need them?
Keys are constant strings values that uniquely identifies a list item among its siblings
Keys help React identify which items have changed, are added, or are removed.
Keys are necessary because reconciling list elements differences without them is highly inefficient

# What are Controlled and Uncontrolled components in React?
Both are ways to implement form controls in React
Controlled: form data is handled by a React component
Uncontrolled: form data is handled by the DOM itself
Controlled components are the recommended way to implement forms
Uncontrolled components are an option when converting legacy code bases to React, or integration with a non-React library¹

Error Boundaries are React components that catch JavaScript errors anywhere in their child component tree, log those errors, and display a fallback UI

# Why should async calls be made in componentDidMount and not the constructor?
A common misconception is that fetching data in the constructor avoids an additional rendering step compared to componentDidMount
Reality: Fetching data in the constructor offers no performance improvements over componentDidMount¹
Data won’t be loaded if the async request in constructor completes after the component mounts
Best practices are to avoid side effects in constructor
In the constructor, the state should be initialized andsetState() should not be called²
(B) Data fetching via async calls can be managed using the useEffect hook³
(B) React Suspense is a potential alternative to fetch data in the future⁴

# What are React Hooks?
New feature in React 16.8
Allows function components to use state and other previous class-only features


## React Cheat Sheet Full Story
 
A React Element is what gets returned from components. It's an object that virtually describes the DOM nodes that a component represents.
						Or
What exactly is a React element? It’s a VIRTUAL element describing a DOM element. It’s what the React.createElement API method returns.

# What Is React?
React is defined as a JavaScript library for building user interfaces. React is a JavaScript “library”. It is not exactly a “framework”. It is not a complete solution and you will often need to use more libraries with React to form any solution. 

# React’s tree reconciliation?
Before React, when we needed to work with a browser’s API, which is known as the DOM API, we avoided traversing the DOM tree as much as possible and there is a reason for that. Any operation on the DOM is done in the same single thread that’s responsible for everything else that’s happening in the browser, including reactions to user events like typing, scrolling, resizing, etc.
Any expensive operation on the DOM means a slow and janky experience for the user.
React came up with a unique concept to help us do exactly that!

Eg:	document.getElementById('mountNode').innerHTML = `
 <div>
   Hello HTML
 </div>
`;


When we tell React to render a tree of elements in the browser, it first generates a virtual representation of that tree and keeps it around in memory for later.Then it’ll proceed to perform the DOM operations that will make the tree show up in the browser.
When we tell React to update the tree of elements it previously rendered, it generates a new virtual representation of the updated tree. Now React has 2 versions of the tree in memory!
To render the updated tree in the browser, React does not discard what has already been rendered. Instead, it will compare the 2 virtual versions of the tree that it has in memory, compute the differences between them, figure out what sub-trees in the main tree need to be updated, and only update these sub-trees in the browser.

 The other reasons why I think React gained its massive popularity:
Working with the DOM API is hard. React gives developers the ability to work with a “virtual” browser that is friendlier than the real browser. React basically acts like your agent who will do the communication with the DOM on your behalf.
React is often given the “Just JavaScript” label. So very small learning curve for js Developers.
Learning React pays off big-time for iOS and Android mobile applications as well. React Native allows you to use your React skills to build native mobile applications. You can even share some logic between your web, iOS, and Android applications.

The ReactDOM.render method and React.createElement method are the core API methods in a React application. In fact, a React web application cannot exist without using both of these methods.

# ReactDOM.render
This is basically the entry point for a React application into the browser’s DOM. It takes 2 arguments : what to render (This is always a “React element”),  WHERE to render that React element in the browser (This has to be a valid DOM <document object model>node).

# React.createElement
Instead of working with strings to represent DOM elements. in React we represent DOM elements with objects using calls to the React.createElement method. These objects are known as React elements. React elements are created in memory. To actually make a React element show up in the DOM, we use the ReactDOM.render method which will do many things to figure out the most optimal way to reflect the state of a React element into the actual DOM tree in the browser.  Only used with jsx as browsers don't understand jsx.

# React is all about components
We define small components and then put them together to form bigger ones. All components small or big are reusable, even across different projects.You can think of components as simple functions, their input is a set of “props” and their output is a description of a UI.

Side effects are the easier concept. A "pure function" is a function that maps its input value(s) into an output value function plus(x, y) { return x + y; }. A "side effect" is any effect other than that return value.

# Why is React named “React” anyway?
When the state of a React component (which is part of its input) changes, the UI it represents (its output) changes as well.In a React application we don’t do that manually. React will simply react to the state changes and automatically (and efficiently) update the DOM when needed.

A compiler that translates one form of syntax into another is known as a “transpiler”.
The name of the component has to start with a capital letter. A JSX compiler (like Babel) will consider all names that start with a lowercase letter as names of HTML elements. 

# JSX is not a template language
Some libraries that deal with HTML provide a template language for it. You write your dynamic views with an “enhanced” HTML syntax that has loops and conditionals. These libraries will then use JavaScript to convert the templates into DOM operations. The DOM operations can then be used in the browser to display the DOM tree described by the enhanced HTML.React eliminates that step. We do not send to the browser a template at all with a React application. We sent it a tree of objects described with the React API. React uses these objects to generate the DOM operations needed to display the desired DOM tree.
Creating components using classes

a class extends React.Component . A class-based React component has to at least define an instance method named render. You access props as this.props
Functions vs classes

The only way to make a component “stateful” was to use the class syntax. This has changed with the release of “React Hooks” beginning with React version 16.8, which was released in early 2019.

In a component, state is data we import. Stateful and stateless components have many different names.
They are also known as:
– Container vs Presentational components
– Smart vs Dumb components
The literal difference is that one has state, and the other doesn’t. That means the stateful components are keeping track of changing data, while stateless components print out what is given to them via props, or they always render the same thing.
Components vs Elements
A React Component is a template,This can be either a function or a class
A React Element is what gets returned from components. It’s an object that virtually describes the DOM nodes that a component represents. React elements are not what you see in the browser. They are just objects.
What exactly are hooks?
A hook in a React component is a call to a special function. All hooks functions begin with the word “use”. Some of them can be used to provide a function component with stateful elements (like useState), others can be used to managed side effects (like useEffect) or to cache/memoize functions and objects (like useCallback).
React hook functions can only be used in function components. You can’t use them in class components.
Responding to user events


You can add an event handler with an “onEvent” property , This could be an onClick, onMouseOver, onScroll, onSubmit, etc.
eg:onClick={() => console.log('Button clicked')}

# Reading and updating state

To track state updates and trigger virtual DOM diffing and real DOM reconciliation, React needs to be aware of any changes that happen to any state elements that are used within components. The useState hook defines a state element and gives us back a getter and setter for it!

const [count, setCount] = React.useState(0);

useState function returns an array with exactly 2 items. The first item is a value (getter) and the second item is a function (setter).
The first item “value” can be a string, number, array, or other types to initial value of the state.
The second item “function” will change the value of the state element when invoked React will re-render the component
Rendering sibling components

ReactDOM.render([<Button />, <Display />], mountNode);
Or
ReactDOM.render(
 <div>
   <Button />
   <Display />
 </div>,
 mountNode
);
				Or
react has a special object if you need to enclose multiple adjacent elements like this without introducing a new DOM parent node. You can use React.Fragment:
ReactDOM.render(
 <React.Fragment>
   <Button />
   <Display />
 </React.Fragment>,
 mountNode
);
Instead of typing React.Fragment, you can just use an empty tag <></>

# The top-level component

The top-level component is popularly used to manage shared application state and actions because it’s parent to all other components. Be careful about this design because updating a state element on the top-level component means that the whole tree of components will be re-rendered (in memory).

	The super keyword refers to the parent class. It is used to call the constructor of the parent class and to access the parent's properties and methods.

# Why Immutability Is Important?
There are generally two approaches to changing data. The first approach is to mutate the data by directly changing the data’s values. The second approach is to replace the data with a new copy which has the desired changes.

Data Change with Mutation

var player = {score: 1, name: 'Jeff'}; 
player.score = 2;

Data Change without Mutation

var player = {score: 1, name: 'Jeff'};
var newPlayer = Object.assign({}, player, {score: 2});
The end result is the same but by not mutating (or changing the underlying data) directly, we gain several benefits described below.




# useEffect in action:
useEffect( () => console.log("mount"), [] );
useEffect( () => console.log("will update data1"), [ data1 ] );
useEffect( () => console.log("will update any") );
useEffect( () => () => console.log("will update data1 or unmount"), [ data1 ] );
useEffect( () => () => console.log("unmount"), [] );

 
 
 
 
 
 
 
 
 







