from postdatabase.consulta_sql import ConsultaSQL


def main():
    query = """
    SELECT 
        tp.fl_situacao_rua AS "Situacao de rua", 
        tp.fl_trajetoria_rua AS "Trajetoria de rua", 
        COUNT(*) AS quantidade
    FROM atendimento.tb_pessoa tp 
    WHERE 
        tp.fl_situacao_rua = TRUE OR 
        tp.fl_trajetoria_rua = TRUE
    GROUP BY 
        tp.fl_situacao_rua, 
        tp.fl_trajetoria_rua;
    """

    ConsultaSQL().run(query, 'resultado_consulta.csv')


if __name__ == '__main__':
    main()
