from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from postdatabase.consulta_sql import ConsultaSQL


@pytest.fixture
def consulta_sql():
    return ConsultaSQL()


@patch('consulta_sql.psycopg2.connect')
@patch('consulta_sql.pd.read_sql_query')
def test_execute_query(mock_read_sql_query, mock_connect, consulta_sql):
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn
    mock_df = pd.DataFrame(
        {
            'Situacao de rua': [True],
            'Trajetoria de rua': [False],
            'quantidade': [10],
        }
    )
    mock_read_sql_query.return_value = mock_df

    query = 'SELECT * FROM teste;'
    df = consulta_sql.execute_query(query)

    mock_connect.assert_called_once()
    mock_read_sql_query.assert_called_once_with(query, mock_conn)
    pd.testing.assert_frame_equal(df, mock_df)


@patch('consulta_sql.psycopg2.connect')
def test_connect_disconnect(mock_connect, consulta_sql):
    consulta_sql.connect()
    mock_connect.assert_called_once()

    consulta_sql.disconnect()
    assert consulta_sql.conn is None


@patch('consulta_sql.pd.read_sql_query')
@patch('consulta_sql.ConsultaSQL.save_to_csv')
@patch('consulta_sql.ConsultaSQL.connect')
@patch('consulta_sql.ConsultaSQL.disconnect')
def test_run(
    mock_disconnect,
    mock_connect,
    mock_save_to_csv,
    mock_read_sql_query,
    consulta_sql,
):

    mock_df = pd.DataFrame(
        {
            'Situacao de rua': [True],
            'Trajetoria de rua': [False],
            'quantidade': [10],
        }
    )
    mock_read_sql_query.return_value = mock_df

    query = 'SELECT * FROM teste;'
    output_file = 'teste.csv'
    consulta_sql.run(query, output_file)

    mock_connect.assert_called_once()
    mock_read_sql_query.assert_called_once_with(query, consulta_sql.conn)
    mock_save_to_csv.assert_called_once_with(mock_df, output_file)
    mock_disconnect.assert_called_once()
