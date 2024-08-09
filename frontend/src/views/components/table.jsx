import React from 'react'

import Spinner from 'react-bootstrap/Spinner'
import Button from 'react-bootstrap/Button'
import BootstrapTable from 'react-bootstrap-table-next'

const Table = (props) => {
  return (
    <>
      {props.isLoading ? (
        <Spinner animation='border' role='status' />
      ) : (
        <>
          <BootstrapTable
            keyField={props.keyField}
            data={props.data}
            columns={props.columns}
            bordered={props?.bordered}
            hover={props?.hover}
            pagination={props?.pagination}
            remote={props?.remote}
            onTableChange={props?.onTableChange}
          />
          {props.cursorPagination && (
            <>
              <Button
                variant='primary'
                type='submit'
                disabled={!props.previousToken}
                onClick={props.previousOnClick}
              >
                Previous
              </Button>
              <Button
                variant='primary'
                type='submit'
                disabled={!props.nextToken}
                onClick={props.nextOnClick}
              >
                Next
              </Button>
            </>
          )}
        </>
      )}
    </>
  )
}

export default Table
