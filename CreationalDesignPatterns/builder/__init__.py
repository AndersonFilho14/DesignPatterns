# The Product: Nf and NfItem classes
class NfItem:
    def __init__(
        self,
        codigo_referencia: str,
        item_descricao: str,
        item_ncm: str,
        item_cest: str,
        item_cfop: str,
        item_unidade_compra: str,
        item_quantidade_compra: Decimal,
        item_valor_unitario: Decimal,
        item_valor_produto: Decimal,
        item_nr_montadora: str,
    ) -> None:
        self.codigo_referencia = codigo_referencia
        self.item_descricao = item_descricao
        self.item_ncm = item_ncm
        self.item_cest = item_cest
        self.item_cfop = item_cfop
        self.item_unidade_compra = item_unidade_compra
        self.item_quantidade_compra = item_quantidade_compra
        self.item_valor_unitario = item_valor_unitario
        self.item_valor_produto = item_valor_produto
        self.item_nr_montadora = f"00{item_nr_montadora}"

    def __repr__(self) -> str:
        return (
            f"NfItem(codigo_referencia='{self.codigo_referencia}', "
            f"item_descricao='{self.item_descricao}', "
            f"item_ncm='{self.item_ncm}', "
            f"item_cest='{self.item_cest}', "
            f"item_cfop='{self.item_cfop}', "
            f"item_unidade_compra='{self.item_unidade_compra}', "
            f"item_quantidade_compra={self.item_quantidade_compra}, "
            f"item_valor_unitario={self.item_valor_unitario}, "
            f"item_valor_produto={self.item_valor_produto}, "
            f"item_nr_montadora='{self.item_nr_montadora}')"
        )


class Nf:

    def __init__(
        self,
        loja: str,
        loja_emitente: str,
        data_emissao: str,
        chave_nf: str,
        nf: str,
        total: Decimal,
    ) -> None:
        self.loja = loja
        self.loja_emitente = loja_emitente
        self.data_emissao = data_emissao
        self.chave_nf = chave_nf
        self.nf = nf
        self.total = total
        self.xml_x64 = ""
        self.nf_itens: list[NfItem] = []

    def set_nf_item(self, nf_item: NfItem):
        self.nf_itens.append(nf_item)

    def set_xml_x64(self, xml_x64: str) -> None:
        self.xml_x64 = xml_x64

    def __repr__(self):
        return (
            f"Nf(loja='{self.loja}', loja_emitente='{self.loja_emitente}', "
            f"data_emissao='{self.data_emissao}', chave_nf='{self.chave_nf}', "
            f"nf='{self.nf}', total={self.total}, "
            f"itens={self.nf_itens})"
        )


# Builder Interface (Abstract Base Class)
class INfBuilder(ABC):

    @abstractmethod
    def build_header(self) -> "INfBuilder":
        pass

    @abstractmethod
    def build_items(self) -> "INfBuilder":
        pass

    @abstractmethod
    def get_result(self) -> Nf:
        pass


# Concrete Builder
class NfBuilder(INfBuilder):

    def __init__(self, xml_data: dict):
        self._xml_data = xml_data
        self._nf = None

    def build_header(self) -> "NfBuilder":
        header_data = self._xml_data.get(ChavesRetornoEnum.CABECALHO, {})

        self._nf = Nf(
            loja=header_data.get(ChavesCabecalhoEnum.LOJA),
            loja_emitente=header_data.get(ChavesCabecalhoEnum.LOJA_EMITENTE),
            data_emissao=header_data.get(ChavesCabecalhoEnum.DATA_EMISSAO),
            nf=header_data.get(ChavesCabecalhoEnum.NUMERO_NF),
            chave_nf=header_data.get(ChavesCabecalhoEnum.CHAVE_NF),
            total=header_data.get(ChavesCabecalhoEnum.VALOR_TOTAL),
        )
        return self

    def build_items(self) -> "NfBuilder":
        if not self._nf:
            raise ValueError("Fiscal note header must be built first.")

        item_data_list = self._xml_data.get(ChavesRetorn oEnum.ITENS, [])

        for item_data in item_data_list:
            item = NfItem(
                codigo_referencia=item_data.get(ChavesItemEnum.CODIGO_REFERENCIA),
                item_descricao=item_data.get(ChavesItemEnum.DESCRICAO),
                item_ncm=item_data.get(ChavesItemEnum.NCM),
                item_cest=item_data.get(ChavesItemEnum.CEST),
                item_cfop=item_data.get(ChavesItemEnum.CFOP),
                item_unidade_compra=item_data.get(ChavesItemEnum.UNIDADE_COMPRA),
                item_quantidade_compra=item_data.get(ChavesItemEnum.QUANTIDADE_COMPRA),
                item_valor_unitario=item_data.get(ChavesItemEnum.VALOR_UNITARIO),
                item_valor_produto=item_data.get(ChavesItemEnum.VALOR_PRODUTO),
                item_nr_montadora=item_data.get(ChavesItemEnum.NUMERO_MONTADORA),
            )
            self._nf.set_nf_item(item)

        return self

    def get_result(self) -> Nf:
        if not self._nf:
            raise ValueError("NF object has not been built. Call build_header() first.")
        return self._nf

# Director Builder
class NfDirector:
    def __init__(self, builder: INfBuilder):
        self._builder = builder

    def construct_from_xml(self) -> Nf:
        return self._builder.build_header().build_items().get_result()


# --- Client Code ---
xml_data_example: dict = {...}
nf_builder = NfBuilder(xml_data=xml_data_example)
director = NfDirector(builder=nf_builder)
nf_object: Nf = director.construct_from_xml()
