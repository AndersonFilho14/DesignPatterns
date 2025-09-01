# builder

`separate the construction of an obj from its represantation`
creat a builder class containing the same filds of the object you need created
ADd several setter-methods for these filds and a "build" method responsible for creatinh the object
Think about creatinhh a director if the same creation code is used to creat several objects (if create a DIRECTOR client must create both the builder and the direcotr) 

Usalo quando o obj a ser criado tem muitos paramentors

## categorias 
The Builder interface declares product construction steps that are common to all types of builders.

Concrete Builders provide different implementations of the construction steps. Concrete builders may produce products that don’t follow the common interface.

Products are resulting objects. Products constructed by different builders don’t have to belong to the same class hierarchy or interface.

The Director class defines the order in which to call construction steps, so you can create and reuse specific configurations of products.

The Client must associate one of the builder objects with the director. Usually, it’s done just once, via parameters of the director’s constructor. Then the director uses that builder object for all further construction. However, there’s an alternative approach for when the client passes the builder object to the production method of the director. In this case, you can use a different builder each time you produce something with the director.


## Director 

In addition, the director class completely hides the details of product construction from the client code. The client only needs to associate a builder with a director, launch the construction with the director, and get the result from the builder.


## Aplication 

Use the Builder pattern to get rid of a “telescoping constructor”.

