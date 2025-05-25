#!/bin/bash
set -e

mongosh <<EOF

use $MONGO_INITDB_DATABASE

db.constant.insertMany( [
   {
      _id: Int32(0),
   },
   {
      _id: Int32(1),
   },
   {
      _id: Int32(2),
   }
]);

db.count_rows.insertMany( [
   {
      _id: Int32(0),
   },
   {
      _id: Int32(1),
   },
   {
      _id: Int32(2),
   }
]);

db.primitives.insertMany( [
    {
        _id: ObjectId('171e75500ecde1c75c59139e'),
        a: true,
        b: Int32(42),
        c: Long(23423),
        d: 1.22,
        e: "hello",
        f: Binary.createFromHexString("aaaa"),
    },
    {
        _id: ObjectId('271e75500ecde1c75c59139e'),
        a: false,
        b: Int32(13),
        c: Long(13),
        d: 1.23,
        e: "hi",
        f: Binary.createFromHexString("abab"),
    },
    {
        _id: ObjectId('371e75500ecde1c75c59139e'),
        a: false,
        b: Int32(15),
        c: Long(15),
        d: 1.24,
        e: "bye",
        f: Binary.createFromHexString("acac"),
    }
]);

db.missing.insertMany( [
    {
        _id: ObjectId('171e75500ecde1c75c59139e'),
        b: Int32(32),
        c: Long(23423),
        d: 1.1,
        e: "hello",
    },
    {
        _id: ObjectId('271e75500ecde1c75c59139e'),
        a: true,
        b: Int32(64),
        d: 1.2,
        f: Binary.createFromHexString("abcd"),
        x: NumberDecimal("9823.1297"),
    },
    {
        _id: ObjectId('371e75500ecde1c75c59139e')
    },
]);

db.column_selection_A_b_C_d_E.insertMany( [
   {
      _id: Int32(0),
      COL1: Int32(1),
      col2: Int32(2),
   },
   {
      _id: Int32(1),
      COL1: Int32(10),
      col2: Int32(20),
   }
]);

db.column_selection_COL1.insertMany( [
   {
      _id: Int32(0),
      COL1: Int32(1),
      col2: Int32(2),
   },
   {
      _id: Int32(1),
      COL1: Int32(10),
      col2: Int32(20),
   }
]);

db.column_selection_col2_COL1.insertMany( [
   {
      _id: Int32(0),
      COL1: Int32(1),
      col2: Int32(2),
   },
   {
      _id: Int32(1),
      COL1: Int32(10),
      col2: Int32(20),
   }
]);

db.column_selection_col2.insertMany( [
   {
      _id: Int32(0),
      COL1: Int32(1),
      col2: Int32(2),
   },
   {
      _id: Int32(1),
      COL1: Int32(10),
      col2: Int32(20),
   }
]);

db.column_selection_col3.insertMany( [
   {
      _id: Int32(0),
      COL1: Int32(1),
      col2: Int32(2),
   },
   {
      _id: Int32(1),
      COL1: Int32(10),
      col2: Int32(20),
   }
]);

EOF