class Singleton:
    instancia = None

    def __new__(cls, *args, **kwargs):
        if cls.instancia is None:
            cls.instancia = super().__new__(cls)
        return cls.instancia

    def __init__(self, nome: str):
        self.__nome = nome


    def mostrar_nome(self) -> None:
        print(f"nome = {self.__nome}")


if __name__ == '__main__':
    print(Singleton.instancia)
    primeiro = Singleton(nome="primeiro_nome")

    print(Singleton.instancia)

    segundo = Singleton(nome="segundo _nome")
    segundo.mostrar_nome()
