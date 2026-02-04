# Java Design Patterns RAG

## Description of the Document Selected

I selected a document about design patterns. They came from a website. Initially I tried web scraping the site but it has protections against that.

---

## 3 Questions and Responses

### Question 1: Tell me about Creational Patterns.

**Answer:** Creational patterns deal with the process of object creation in software development. They help to abstract the instantiation process, making the code more flexible, reusable, and maintainable. These patterns enable developers to create objects in a way that suits their system's needs, leading to better management of object creation mechanisms and improved ease of use. Examples of creational patterns include the Singleton pattern, which ensures that a class has only one instance, among others.

---

### Question 2: Tell me the difference between the Factory Pattern and the Abstract Pattern

**Answer:** The Factory Pattern provides an interface for creating objects in a superclass, allowing subclasses to decide which class to instantiate. It emphasizes loose coupling by eliminating the need for clients to know about the concrete classes, typically focusing on creating a single object or a specific family of objects.

In contrast, the Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. It allows switching between different product families at runtime and is used when a system needs to be independent of how its objects are created, composed, and represented.

In summary, the Factory Pattern deals with the instantiation of a single product, while the Abstract Factory Pattern deals with the instantiation of families of products.

---

### Question 3: Tell me about Bridge Pattern

**Answer:** The Bridge Pattern decouples an abstraction from its implementation, allowing them to vary independently. This design pattern is useful when you want to separate the interface from its implementation, enabling both to evolve separately.

An example of the Bridge Pattern is a Shape class that utilizes different rendering methods. It involves an interface `Renderer` with a method `renderShape(Shape shape)` and an implementation class, `VectorRenderer`, that implements this interface by providing the specific rendering logic.

The primary focus of the Bridge Pattern is to facilitate flexibility in changing the abstraction and its implementation independently without affecting each other.

---

### Observation

The quality of these answers is surprising given they were generated with the smallest chunk-overlap size. The answers are brief largely reflect the text in the document and when the system didn't know the answer it said that instead of hallucinating an answer.

---

## Chunk-Size and Overlap Experiments

**Observation:** Initially when I increase the chunk overlap size the answers became more detailed. However when I increased it from 100 to 500 the quality of the answer dropped significantly.

---

### Chunk Size = 1000; Overlap = 50

**Question:** What patterns can you tell me about?

**Answer:** The context provides information about several design patterns, specifically:

1. **Structural Patterns**:
   - **Adapter Pattern**: Used to allow incompatible interfaces to work together.
   - **Facade Pattern**: Provides a unified interface to a set of interfaces in a subsystem, making it easier to use.
   - **Decorator Pattern**: Allows you to attach additional responsibilities to an object dynamically, providing a flexible alternative to subclassing.

2. **Behavioral Patterns**:
   - **Observer Pattern**: Implements a publish-subscribe model, allowing objects to notify and update multiple components when data changes.
   - **Strategy Pattern**: Allows for the selection of different algorithms or behaviors at runtime.

3. **Creational Patterns**:
   - **Singleton Pattern**: Ensures that a class has only one instance, often used for managing resources like database connections.

Additionally, examples of other patterns mentioned include:
- **Factory Method**: Used for creating objects for different file formats.

These patterns help in improving code readability, maintainability, and facilitate structured communication in software development.

---

### Chunk Size = 1000; Overlap = 100

**Question:** What patterns can you tell me about?

**Answer:** The context provides information about several design patterns, including:

1. **Structural Patterns**: These patterns focus on the composition of classes and objects to create larger structures while maintaining relationships between components.
   - **Adapter Pattern**: Allows for the integration of incompatible interfaces.
   - **Facade Pattern**: Provides a unified interface to a set of interfaces in a subsystem, simplifying system use.
   - **Decorator Pattern**: Enables attaching additional responsibilities to objects dynamically, offering flexibility over subclassing.

2. **Behavioral Patterns**: These define how objects interact and communicate with one another to streamline communication and promote flexibility and maintainability.
   - **Example not explicitly named** but demonstrates a proxy mechanism with `ImageProxy` that delays image loading until it's needed.

3. **Creational Patterns**: These deal with the object creation process, making it more flexible, reusable, and maintainable.
   - **Singleton Pattern**: Ensures a class has only one instance, often used for managing resources like database connections or logging.

Other common design patterns mentioned include:
- **Factory Method**: For creating objects across different formats (e.g., CSV, JSON, XML).
- **Observer**: For implementing publish-subscribe models or updating UI components upon data changes.
- **Strategy**: For supporting various payment methods in applications or different sorting algorithms.

Please let me know if you need information on a specific pattern or concept!

---

### Chunk Size = 1000; Overlap = 500

**Question:** What patterns can you tell me about?

**Answer:** The context provides information about several design patterns, including:

1. **Structural Patterns**: These patterns focus on the composition of classes and objects to create larger structures while maintaining relationships between components. An example mentioned is the **Adapter Pattern**.

2. **Behavioral Patterns**: These patterns define how objects interact and communicate with one another, helping to streamline communication between components and promote flexible and maintainable systems. An example mentioned is the **ImageProxy** class.

3. **Singleton**: This pattern ensures that only a single instance of a particular class, such as a database connection or a logging class, exists in the application.

4. **Factory Method**: This pattern is used for creating objects, especially when dealing with different file formats like CSV, JSON, or XML parsers.

5. **Observer**: This pattern implements a publish-subscribe model, commonly seen in messaging systems.

These patterns help in faster development, easier communication among team members, and provide reusable solutions to common problems in software design.

---

## 5 Important Questions and Answers

I have tried asking the RAG system:

> **Question:** What are five important questions to understand this RAG system (e.g., about embedding dimensionality, FAISS search behavior, chunk overlap, prompt design)? Include the answer with your response to each question.
>
> **Answer:** I don't know.

> **Question:** What are five important questions to understand this RAG system?
>
> **Answer:** I don't know.

When I asked Claude:

### 1. What is the embedding dimensionality and why does it matter?

The all-distilroberta-v1 model produces 768-dimensional vectors. Each chunk and query becomes a point in 768-dimensional space. Higher dimensions capture more semantic nuance but require more memory/compute. FAISS uses these vectors to find chunks semantically similar to queries via distance calculations.

### 2. How does FAISS IndexFlatL2 search work?

IndexFlatL2 performs brute-force L2 (Euclidean) distance search - it compares the query vector against every stored vector. Lower distance = more similar. It's exact (not approximate) but O(n) per query. For large datasets, you'd use approximate indexes like IndexIVFFlat for speed, trading some accuracy.

### 3. Why use chunk overlap, and what's the tradeoff with 50 vs 100?

Overlap (chunk_overlap=50) ensures context isn't lost at chunk boundaries. If a concept spans two chunks, overlap preserves it in both. 50 chars = minimal redundancy but risks splitting sentences. 100 chars = safer context preservation but more redundant storage and potentially duplicate retrieval results.

### 4. Why use a two-stage retrieval (bi-encoder → cross-encoder)?

- **Bi-encoder + FAISS**: Fast but approximate - encodes query and chunks independently
- **Cross-encoder**: Slow but accurate - jointly scores (query, chunk) pairs

Retrieving top_k=20 with the fast bi-encoder, then re-ranking to top_m=8 with the cross-encoder gives you the speed of vector search with the accuracy of cross-attention. Best of both worlds.

### 5. How does prompt design affect answer quality?

Your prompt uses:

- **System prompt**: Sets behavior ("answer from context, say 'don't know' if missing")
- **User prompt**: Provides context first, then question

This "context-before-question" format helps the LLM attend to relevant information. The explicit "say you don't know" instruction reduces hallucination.
