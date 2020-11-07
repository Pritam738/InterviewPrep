# What is React?
React is a JavaScript library for building user interfaces. It is developed by Facebook.

# What are React’s Key Features?
1)Virtual DOM

2)JSX

3)Unidirectional Data Flow

4)Server-Side Rendering

## What is JSX?
JSX is a Javascript syntax extension that allows us to write HTML in our JavaScript to create React Elements

Babel compiles JSX into React.createElement() calls

Cleaner code with JSX expressions

Safer code as the usage of JSX prevents XSS attacks


## What is the Virtual DOM?
Manipulating the actual DOM is expensive

Virtual DOM: React makes a virtual representation of the actual DOM in memory

Expected changes are first reflected in an updated version of the Virtual DOM. The updated virtual DOM is compared with its previous version using React’s 

‘diffing’ algorithm to determine how to best update the real DOM

## What is uni directional data flow ?
The data flows from the parents to the child and not the other way round. 

- [] What is the benefit of this? 

# Workings of React framework

# Reconciliation
React provides a declarative API so that you don’t have to worry about exactly what changes on every update. This makes writing applications a lot easier, but it might not be obvious how this is implemented within React.

When you use React, at a single point in time you can think of the render() function as creating a tree of React elements. On the next state or props update, that render() function will return a different tree of React elements. React then needs to figure out how to efficiently update the UI to match the most recent tree.

There are some generic solutions to this algorithmic problem of generating the minimum number of operations to transform one tree into another. However, the state of the art algorithms have a complexity in the order of O(n3) where n is the number of elements in the tree.

If we used this in React, displaying 1000 elements would require in the order of one billion comparisons. This is far too expensive. Instead, React implements a heuristic O(n) algorithm based on two assumptions:

Two elements of different types will produce different trees.
The developer can hint at which child elements may be stable across different renders with a key prop.

## The Diffing Algorithm

When diffing two trees, React first compares the two root elements. The behavior is different depending on the types of the root elements. Such as :

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

# class component
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
# function component

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
Class lifecycle methods split up related pieces of code.

# What causes a component to update?
A re-render of the parent which may entail new Props
setState()
(B) forceUpdate() (and that it should be avoided!)

# What are props and state in React?
props is the JavaScript object, passed into a Component, that holds the configuration properties¹
props is immutable by the receiving Component
state is the JavaScript object, managed within the Component, that holds its internal state.
Updates to either trigger a re-render

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
