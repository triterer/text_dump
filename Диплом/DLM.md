DLM
========================

Как мы блокируем узлы в одном файле?
Мы добавлям замок в 

Как мы блокируем узлы в нескольких файлах?

Как мы перносим структуру мз Schema Registry в DLM?

Как мы действуем при расширении схемы?

Как синхронизируются замки в DLM?

Как блкируемся при транзитивных запросах, например join?

Как хранить список документов в коллекции и как его обновлять?


Стурктура узла

```rust
enum NodeTypes {
    SCALAR,
    ARRAY,
    OBJECT
}

enum LockType {
    IntentShared,  
    IntentExclusive,
    Shared,
    Exclusive
}

struct Lock {
    lock_type: LockType,
    transaction_id: String
}

struct node {
    path: String,
    node_type: node_types,
    granted_locks: Vec(lock),
    locks_queue: Vec(lock),
    childrens: Vec(node)
}
```

Фактически мы храним два слоя. Первый слой это первое общее дерево в котором есть все узлы коллекции. На него мы вешаем разные сканирования, как например where или join. Потом мы динамически формируем блокировки дерева для конкретных документов.